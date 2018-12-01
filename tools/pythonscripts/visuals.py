import re, os
import numpy as np
from NMRFxMolProbTools import NMRFxMolProbTools
from collections import OrderedDict
import matplotlib as mpl
import matplotlib.pyplot as plt


class ShowMolProbAnalysis(object):
    def __init__(self, rel_path, file_name="mpola.txt"):
        self.rel_path = rel_path
        self.home = os.getenv("HOME")
        self.file_name = file_name

    def _nav_and_grab(self):
        """Function navigates to the directory and retrieves the output file of MolProbity's one-line analysis. """
        if isinstance(self.rel_path, str):
            if os.path.exists(self.rel_path):
                if os.path.isfile(self.rel_path):
                    # Pass a file path directly
                    pmp = NMRFxMolProbTools()
                    mp_organized_dict = pmp.org_molprobity_output(self.rel_path)
                    return mp_organized_dict
                elif os.path.isdir(self.rel_path) and os.path.exists(self.rel_path+"/"+self.file_name):
                    # Pass a directory containing the file
                    pmp = NMRFxMolProbTools()
                    mp_organized_dict = pmp.org_molprobity_output(self.rel_path+"/"+self.file_name)
                    return mp_organized_dict
                else:
                    if os.path.isdir(self.rel_path):
                        # Pass a directory containing directories; checks for directories of structures
                        ls_dir = os.listdir(self.rel_path)
                        # PDB ID regex
                        pat = re.compile(r'([1-9][a-z0-9]{3})', re.I)
                        summary_per_struc = []
                        for i, elem in enumerate(ls_dir):
                            match = pat.search(elem)
                            if match:
                                selection = match.group(1)
                                sel_path = self.rel_path+"/"+selection
                                if os.path.isdir(sel_path):
                                    # Found directory of structure in list... now look for file
                                    analysis_file_path = ""
                                    for root, _, afile in os.walk(sel_path):
                                        if self.file_name in afile:
                                            analysis_file_path = root+"/"+self.file_name
                                    if analysis_file_path:
                                        pmp = NMRFxMolProbTools()
                                        processed_dict = pmp.org_molprobity_output(analysis_file_path)
                                        summary = pmp.run_descriptive_stats(processed_dict)
                                        summary_per_struc.append((selection, summary))
                        if summary_per_struc:
                            return summary_per_struc
                        else:
                            raise OSError("File '{}' not found. Check directory or specify 'file_name'.".format(self.file_name))
            else:
                raise ValueError("Could not find relative path used as input. Does not exist.")

    def show_one_struc(self):
        mp_orgnized_dict = self._nav_and_grab()
        assert (type(mp_orgnized_dict) is OrderedDict), ""
        if mp_orgnized_dict:
            obj_arr = ['f{}'.format(file_name.split('.')[0][-1]) for file_name in mp_orgnized_dict['#pdbFileName']]
            index = np.arange(len(obj_arr))
            i = 1
            check_list = NMRFxMolProbTools.check_list
            for k in check_list:
                if k == 'numPperp' or k == 'numSuites':
                    continue
                else:
                    try:
                        value = mp_orgnized_dict[k]
                        if value[0]:
                            value = list(map(float, value))
                        else:
                            continue
                    except KeyError:
                        continue
                    ax = plt.subplot(2, 3, i)
                    ax.bar(index, value, align='edge', width=.5)
                    plt.ylabel(k)
                    plt.ylim(ymin=0)
                    plt.xticks(index, obj_arr)
                    i += 1
            plt.show()

    def show_mult(self):
        """ This function receives a list of tuples whose first element is the structure name (i.e. '2koc')
        and the second element is a dictionary of whose keys are the MolProbity analysis parameter names and whose values
        are dictionaries that summarize descriptive statistical values. """

        # Input list_data example :
        # [('1khm', {'MolProbityScore': {'var': 0.013, 'std': 0.112, 'mean': 2.4516},
        # 'clashscore': {'var': 2.724, 'std': 1.651, 'mean': 4.21},
        # 'numbadbonds': {'var': 0.0, 'std': 0.0, 'mean': 0.0},
        # 'ramaOutlier': {'var': 1.44, 'std': 1.2, 'mean': 5.40},
        # 'rota<1%': {'var': 1.247, 'std': 1.117, 'mean': 3.45},
        # 'numbadangles': {'var': 2.81, 'std': 1.676, 'mean': 5.70}}),
        # ('1z2q', {'MolProbityScore': {'var': 0.027, 'std': 0.163, 'mean': 1.98}, ...
        # 'numbadangles': {'var': 1.087, 'std': 1.043, 'mean': 7.75}})]

        list_data = self._nav_and_grab()

        # Grabbing all of the structure names defined
        pid_object = [name[0] for name in list_data]

        # Defining an index used as a bar plot parameter
        index = np.arange(len(pid_object))

        # Dictionary that pairs the keys of input list_data to the formalize title used in plots
        opts = OrderedDict([
            ('clashscore', 'Clashscore'),
            ('MolProbityScore', 'MolProbity Score'),
            ('rota<1%', 'Rotameric Outliers'),
            ('ramaOutlier', 'Ramanchandran Outliers'),
            ('pct_Suites', 'Suite Outliers (%)'),
            ('pct_Pperp', 'Pucker Outliers (%)')
            # ('pct_badbonds', 'Bad Bonds (%)'),
            # ('pct_badangles', 'Bad Angles (%)')
        ])

        # filtering input list_data to retrieve specified parameters
        info = []
        for key in opts:
            if key in list_data[1][1]:
                info.append((opts.get(key), [tup[1][key]['mean'] for tup in list_data],
                             [tup[1][key]['std'] for tup in list_data]))

        # defining number of plots
        num_of_subplots = len(info)

        if num_of_subplots > 1:
            # helper iterator value
            k = 0
            # iterate over axes and generate subplots based on the length of the 'info' list
            for i in range(1, num_of_subplots + 1):
                ax = plt.subplot((num_of_subplots + 1) // 2, 2, i)
                ax.bar(index, info[k][1], align='center', yerr=info[k][2], color='r',
                       error_kw=dict(ecolor='gray', lw=2, capsize=0))
                plt.ylabel(info[k][0])
                plt.ylim(ymin=0)
                plt.xticks(index, pid_object)
                k += 1

            # Writes title on figure
            plt.suptitle('NMRFxStructure: RNA Structures', fontsize='20')

            plt.show()


smp = ShowMolProbAnalysis('../../rnastrucs/', file_name='cy_tests_fa.txt')
smp.show_mult()