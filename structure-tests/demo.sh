#!/bin/bash

# This script serves as a demo script for new users with
# machines that run BASH. The purpose of this script is to 
# run all tests we've been using to replenish nmrfxstructure.

# There are 5 RNA structure directories and 10 protein structure directories
# labeled using their PDB ID tag. This script prints all the output information onto
# a directory called 'data'. To evaluate the standard output or standard error of each
# calculation, you can refer to the summary.log file in this directory.  

#running from the structure-supplements/structure-tests/*strucs directory


cwd=`pwd`;
nmrfxs=`find ${HOME} -path "*${HOME}*nmrfxstructure*structure-*-bin*nmrfxs"`;
mkdir -p data;

echo TIMESTAMP: `date` &> summary.log;

for d in ./rnastrucs/*/xp-tests ./rnastrucs/*/cy-tests ./proteinstrucs/*/xp-tests ./proteinstrucs/*/cy-tests;
do
    echo '-------------------------------------------------------';
    echo -e "\t\t$d";
    echo '-------------------------------------------------------';
    cd $d;
    struc=`echo $d | grep -o "[1-9][a-z0-9]*"`;
    mkdir -p  $cwd/data/$struc;
    strucType=`echo $d | grep -o "[a-z]*-tests"`;

    echo $d >> $cwd/summary.log;

    $nmrfxs gen -s 1 project.yaml &>> $cwd/summary.log;

    if [ $? -eq 0 ]; then
        echo 'Successful calculation!';
    elif [ $? -eq 130 ]; then
        echo 'Program interrupted ...';
        exit 1;
    else
        echo 'Failed calculation!';
    fi
    mv output $cwd/data/$struc/$strucType;
    
    cd $cwd;
done

