import unittest
import os, re, random
import subprocess as sp

# finding the root directory (structure-supplements)
home_dir = os.getenv("HOME")
if os.getcwd() is not home_dir:
    os.chdir(home_dir)
found_root = False
for root, _, _ in os.walk("."):
    if 'structure-supplements' in root:
	root_dir = root
	found_root = True
	break
assert (found_root), "Could not find 'structure-supplements' directory where the test suite is located."


class TestCalcEnergy(unittest.TestCase):

    def setUp(self):
        # Initializing prgm location and nmrfxs command. (Update version when necessary!)
	self.sup_dir = home_dir + root_dir[1:]
	self.dump_dir = self.sup_dir + '/test-suite/data'
	self.test_dir = self.sup_dir + '/structure-tests'
	os.chdir(self.test_dir)
        from auxillary_funcs import find_compiled_struct
        self.nmrfxs_cmd = find_compiled_struct()


    def test_cy_RNA_energy(self):
        """Integrated test evaluating energy of an RNA structure (2KOC) using cyana constraints"""
	strc = '2koc'
	strc_dir = '/'.join([self.dump_dir, strc])
        os.chdir("./rnastrucs/"+strc+"/cy_tests")
        cwd = os.getcwd()
        lst_cwd = os.listdir(cwd)
        assert ("project.yaml" in lst_cwd), "No 'project.yaml' found in directory."
	try:
	    if strc not in os.listdir(self.dump_dir):
		os.mkdir(strc_dir)
            test_output = sp.check_output(self.nmrfxs_cmd + " gen -s 3 -d " + strc_dir + " project.yaml", shell=True)
        except sp.CalledProcessError:
            raise RuntimeError("Problem executing nmrfxstructure command. Please evaluate version and required input files.")
        pat = re.compile(r'(energy is [-]?[0-9]+\.[0-9]+)')
        mat = pat.search(test_output)
        if mat:
            sel = mat.group(1)
            value = float(sel.split(' ')[-1])
            self.assertLessEqual(value, 5.0)
        else:
            print "Please evaluate generated output. Energy could not be obtained."


    def test_xp_RNA_energy(self):
        """Integrated test evaluating energy of an RNA structure (2L1V) using xplor constraints"""

	strc = '2l1v'
	strc_dir = '/'.join([self.dump_dir, strc])
        os.chdir("./rnastrucs/"+strc+"/xp_tests")
        cwd = os.getcwd()
        lst_cwd = os.listdir(cwd)
        assert ("project.yaml" in lst_cwd), "No 'project.yaml' found in directory."
	try:
	    if strc not in os.listdir(self.dump_dir):
		os.mkdir(strc_dir)
            test_output = sp.check_output(self.nmrfxs_cmd + " gen -s 3 -d " + strc_dir + " project.yaml", shell=True)
        except sp.CalledProcessError:
            raise RuntimeError("Problem executing nmrfxstructure command. Please evaluate version and required input files.")
        pat = re.compile(r'(energy is [-]?[0-9]+\.[0-9]+)')
        mat = pat.search(test_output)
        if mat:
            sel = mat.group(1)
            value = float(sel.split(' ')[-1])
            self.assertLessEqual(value, 5.0)
        else:
            print "Please evaluate generated output. Energy could not be obtained."

    def test_cy_protein_energy(self):
        """Integrated test evaluating energy of a protein structure (3GB1) using cyana constraints"""

	strc = '3gb1'
	strc_dir = '/'.join([self.dump_dir, strc])
        os.chdir("./proteinstrucs/"+strc+"/cy_tests")
        cwd = os.getcwd()
        lst_cwd = os.listdir(cwd)
        assert ("project.yaml" in lst_cwd), "No 'project.yaml' found in directory."
	try:
	    if strc not in os.listdir(self.dump_dir):
		os.mkdir(strc_dir)
            test_output = sp.check_output(self.nmrfxs_cmd + " gen -s 3 -d " + strc_dir + " project.yaml", shell=True)
        except sp.CalledProcessError:
            raise RuntimeError("Problem executing nmrfxstructure command. Please evaluate version and required input files.")
        pat = re.compile(r'(energy is [-]?[0-9]+\.[0-9]+)')
        mat = pat.search(test_output)
        if mat:
            sel = mat.group(1)
            value = float(sel.split(' ')[-1])
            self.assertLessEqual(value, 5.0)
        else:
            print "Please evaluate generated output. Energy could not be obtained."

print __name__

if __name__ == '__main__':
    unittest.main()

