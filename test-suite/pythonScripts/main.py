import sys

'''
This script is written as a processing script. It will execute the 
processes necessary in other python scripts based on the params
passed in. 
The first argument will always be the path to this file and can be
ignored. The second argument will be the type of testing to
perform. The value is expected to be either ct or mv.


ct denotes commit testing and runs a script that checks to make
sure no adverse change is observed in the energy of a structure.
Currently this only utilizes internal nmrfxstructure validation
criteria and does not incorporate molprobity data.

mv denotes multivariate testing and allows a structure to be
calculated in multiple ways in batch. This tool also provides
visual aides to rapidly asses improvements or disimprovements.
Using mv will require additional command line arguments to
complete. The first is a configuration yaml file to specify
what parameters to change and the overall setup of the project.
The second is optional, and should be mol if molprobity should
be executed and tested on the resulting structures.
'''

sys.argv.pop(0)  #removing the path to this file

method = sys.argv.pop(0)
if method == 'ct':
    import PreCommitEnergy_test
    import unittest
    suite = unittest.TestLoader().loadTestsFromModule(PreCommitEnergy_test)
    unittest.TextTestRunner(verbosity=2).run(suite)
elif method == 'mv':
    import mv_testing
elif method == 'v':
	pass

