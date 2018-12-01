#!/bin/bash

testFileName='p_cy_tests_fa.txt'
proFileName='processed_fa.txt'

for d in ./*/cy_tests;
do
    cd $d;
    for i in filtered_dis_ws reg_distance_ws;
    do
	cd $i/final;
	currd=`pwd`
        echo Current Dir: $currd;
	${HOME}/MolProbity/cmdline/oneline-analysis final_pdbs > ./$testFileName;
        python ${HOME}/summer2018/pythonscripts/ProcessMolProb.py ./$proFileName > ./$proFileName;
	cd ../..
	echo "Test at $d/$i completed!"
    done
    cd ../..;
done
