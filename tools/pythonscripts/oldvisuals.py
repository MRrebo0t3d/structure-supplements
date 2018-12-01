import sys, re
import numpy as np
from NMRFxMolProbTools import NMRFxMolProbTools
from collections import OrderedDict
import matplotlib as mpl
import matplotlib.pyplot as plt
import os


class ShowMolProbAnalysis(object):
    def __init__(self, rel_path):
        self.rel_path = rel_path
        self.home = os.getenv("HOME")

    def _nav_and_grab(self):
        if isinstance(self.rel_path, str):
            # For one structure
            if os.path.exists(self.rel_path) and os.path.isfile(self.rel_path):
                pmp = NMRFxMolProbTools()
                mp_organized_dict = pmp.org_molprobity_output(self.rel_path)
                return mp_organized_dict
            elif os.path.isdir(self.rel_path):
                list_dir = os.listdir(self.rel_path)
                if 'MPola.txt' in list_dir:
                    pmp = NMRFxMolProbTools()
                    mp_organized_dict = pmp.org_molprobity_output(self.rel_path+"/MPola.txt")
                    return mp_organized_dict

    # def show_one(self):
    #     mp_orgnized_dict = self._nav_and_grab()
    #
    #     obj = mp_orgnized_dict['#pdbFileName']
    #     index = np.arange(len(obj))
    #
    #     for key in NMRFxMolProbTools.check_list:
    #         try:
    #             for i in range(1, 4):
    #                 val = [float(elem) for elem in mp_orgnized_dict[key] if elem != '']
    #                 ax = plt.subplot(2, 2, i)
    #                 ax.bar(index, val, align='center')
    #                 plt.ylabel(val])
    #                 plt.ylim(ymin=0)
    #                 plt.xticks(index, pid_object)




def nav_and_grab():
    """This function should be able to grab the location of the file which contains the data from the one-line molprobity
    analysis"""

    def grab_rna_structs():
        """"returns a list of dictionaries containing descriptive stats for all the rna structures"""
        cwd = os.getcwd()
        if cwd is not os.getenv("HOME"):
            os.chdir(os.getenv("HOME"))
        pmp = NMRFxMolProbTools()
        os.chdir("nmrfxs_tests/rnastrucs/")
        ls_of_cwd = os.listdir(os.getcwd())
        pat = re.compile(r'([1-9][a-z0-9]{3})', re.I)
        rna_list_of_dicts = []
        for elem in ls_of_cwd:
            match = pat.search(elem)
            if match:
                selection = match.group(1)
                if os.path.isdir(selection):
                    full_analysis_file = selection+'/cy_tests/compile_tests/final_091218/cy_tests_fa.txt'
                    if os.path.exists(full_analysis_file):
                        processed_dict = pmp.org_molprobity_output(full_analysis_file)
                        summary = pmp.run_descriptive_stats(processed_dict)
                        rna_list_of_dicts.append((selection, summary))
            else:
                continue
        return rna_list_of_dicts

    def grab_protein_structs():
        cwd = os.getcwd()
        if cwd is not os.getenv("HOME"):
            os.chdir(os.getenv("HOME"))
        pmp = NMRFxMolProbTools()
        os.chdir("nmrfxs_tests/proteinstrucs/")
        ls_of_cwd = os.listdir(os.getcwd())
        pat = re.compile(r'([1-9][a-z0-9]{3})', re.I)
        protein_list_of_dicts = []
        for elem in ls_of_cwd:
            match = pat.search(elem)
            if match:
                selection = match.group(1)
                if os.path.isdir(selection):
                    full_analysis_file = selection + '/cy_tests/compile_tests/unt_fin_swp/p_cy_tests_fa.txt'
                    if os.path.exists(full_analysis_file):
                        processed_dict = pmp.org_molprobity_output(full_analysis_file)
                        summary = pmp.run_descriptive_stats(processed_dict)
                        protein_list_of_dicts.append((selection, summary))
            else:
                continue
        return protein_list_of_dicts

    return grab_rna_structs(), grab_protein_structs()


def bar_plot(list_data):
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
            info.append((opts.get(key), [tup[1][key]['mean'] for tup in list_data], [tup[1][key]['std'] for tup in list_data]))

    # defining number of plots
    num_of_subplots = len(info)

    if num_of_subplots > 1:
        # helper iterator value
        k = 0
        # iterate over axes and generate subplots based on the length of the 'info' list
        for i in range(1, num_of_subplots+1):
            ax = plt.subplot((num_of_subplots+1)//2, 2, i)
            ax.bar(index, info[k][1], align='center', yerr=info[k][2], color='r', error_kw=dict(ecolor='gray', lw=2, capsize=0))
            plt.ylabel(info[k][0])
            plt.ylim(ymin=0)
            plt.xticks(index, pid_object)
            k += 1

        # Writes title on figure
        plt.suptitle('NMRFxStructure: RNA Structures', fontsize='20')

        plt.show()
    elif num_of_subplots == 1:
        pass

d = nav_and_grab()
bar_plot(d[0])
