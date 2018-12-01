#!/bin/bash

echo "Running MolProbity Oneline Analysis..."
echo "--------------------------------------------------------------"
for d in ./*;
do
    echo $d;
    #mkdir $d/compile_tests/final_with_filter/molprob_testfiles;
    #mkdir $d/compile_tests/final_without_filter/molprob_testfiles;
    #mv $d/compile_tests/final_with_filter/final*.pdb $d/compile_tests/final_without_filter/molprob_testfiles;
    #mv $d/compile_tests/final_without_filter/final*.pdb $d/compile_tests/final_without_filter/molprob_testfiles;
    cd $d/compile_tests/final_with_filter/;
    ${HOME}/MolProbity/cmdline/oneline-analysis molprob_testfiles > molprob_OLA_wf.txt;
    cd ../final_without_filter/;
    ${HOME}/MolProbity/cmdline/oneline-analysis molprob_testfiles > molprob_OLA_woutf.txt;
    cd ../../..;
    #echo Directories created.
done

exit 1
