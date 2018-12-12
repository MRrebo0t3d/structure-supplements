Author: Teddy Colon
Last update: November 29, 2018

Directory Structure:
|
+ --- structure-supplements/ -> (root)
	|
	+ --- other-tests/ -> (contains nmrfxstructure testing information about scoring, shifts prediction, etc.)
	|	    |
	|	    + --- [rnapredpdb/, rnapredvie/, ...]
        |                   |            |
	|                   |            |	
	|                   |            + --- [demo.sh, example.txt, project.yaml, shifts.txt]
	|                   |
	|                   |
	|                   +--- [demo.sh, pbs.pdb, shifts.txt]
        |
        |
	+ --- stucture-tests/ -> (quick batch of structures any user should be able to run)
        |     |
	|     + --- [proteinstrucs/, rnastrucs/]
	|             |
	|             |
	|             + --- [1D3Z/, 2KID/, … other structures labeled by PDB ID]
	|                    |
	|                    |
        |                    + --- [xp-tests/, cy-tests/, bmrb-files/] -> (tests performed using xplor and cyana constraints)
	|                            |
        |                            |
        |                            + --- [project.yaml, input/] -> (input directory contains all the files necessary to run the calculations)
	|
	|
	+ --- test-suite/ -> (Unit tests to evaluate integrity of nmrfxstructure's codebase)
	|	     |
	|	     + --- [scripts/, pythonScripts/, data/, README.txt]
	|		     |	         |
	|		     |	         |	
	|		     |	         + --- [PreCommitEnergy_test.py, auxillary_funcs.py, mv_testing.py, NMRFxMolProbTools.py, main.py, ...]
	|		     |
	|		     |
	|		     + --- [batch_cleanup, checkpath, nmrfxtester]
	|
	|
	+ --- developer-doc/ -> (Developer and user markdown documentation about nmrfxstructure)
	|      |
	|      |
	|      + --- [docs/, markdown.txt, mkdocs.yml, site/] -> (mkdocs generated project directory and files)
	|              |
        |              |
	|	       + --- [about.md, nmrfxstructure.md, refine.md] -> (markdown files)
	|
	|
	+ --- tools/ -> (arbitrary helper scripts written by developers)
	|
	|
	+ --- dependencies.txt -> (File explaining the dependencies of external programs used during alpha testing phase) 
	|
	|
	+ --- README.txt -> (This file)



Unit test:

It is important to test the software before committing any updates to NMRFxStructure's gitlab repository. One way to quickly test the software is to calculate a series of structures and evaluate their energies. We have composed a few integrated tests which can be used by developers to test the program before committing changes. Below you'll find a thorough description of running these unit tests found in the 'NMRFxsTestSuite' directory from anywhere in your system.

Note: Scripts have been written to grab the lastest version of nmrfxstructure. If you have multiple copies with the same version number, the code will grab the first version it finds. Thus, if errors occur while running the unit tests make sure to check the version number of your nmrfxstructure local copy. Make sure your system does not contain duplicates of the same nmrfxstructure version. If you have multiple versions, an obvious fix is deleting all but the version you wish to test.

Running Pre-commit Test Suite:

1. Before running the test suite, it is important that the programs know where they are. Thus, the first step requires adding the 'scripts' absolute path into your PATH environment variable (i.e export PATH=${PATH}:${absolute_path_of_scripts_dir}). 
   - Note: Although the test suite uses the structures in 'structure-test' directory by default, the environment variable 'TEST' can be set to describe the absolute path which contains the appropriate tests structures.
 
2. Once your system knows where the scripts directory is located, you can execute the pre-commit tests by entering 'nmrfxtester ct' in the command line. This command denotes commit testing and runs a script that checks to make
sure no adverse change is observed in the energy of a structure.
   - Note: 'nmrfxtester' will allow you to run MolProbity validation testing. To execute molprobity functionality, there must be a global environment variable that points to the path of Molprobity cmdline or PATH must already include this path. The environment variable should be set as:export MOLPROB="{path_to_mol_prob}"

In order to see the output data of the 'nmrfxtester', we can turn to the data directory which contains the PDB IDs of the structures that ran in the unit test. Within these directories, we'll see the nmrfxstructure output. This includes an energies.txt file that will append the total energy results onto the end of the file so that you can see the progress of the structures energy values. It is recommended that the data directory is cleared after successfully running all the commit tests. 

*** See the README.txt file to get a complete description of different callable testing types to execute.***

