#!/bin/bash

for d in ./*;
do
    echo $d;
    cd $d;
    #mkdir compile_analysis;
    PDBWOF="compile_tests/final_without_filter/final1.pdb";
    echo Running analysis ....;
    ${HOME}/nmrfxstructure/target/structure-10.2.9-bin/structure-10.2.9/nmrfxstructure score -p $PDBWOF project.yaml;
    if [-d analysis];
    then
        mv analysis analysis_rtd;
        mv analysis_rtd compile_analysis;
    fi

    cd ..;
done
    #${HOME}/nmrfxstructure/target/structure-10.2.9-bin/structure-10.2.9/nmrfxstructure score -p temp0.pdb project.yaml;
    #mv analysis ./compile_analysis
