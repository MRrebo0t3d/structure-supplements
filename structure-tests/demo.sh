#!/bin/bash

# This script serves as a demo script for new users with
# machines that run BASH. The purpose of this script is to 
# run a quick test of all the 

#running from the structure-supplements/structure-tests/*strucs directory
cwd=`pwd`

args=$1;

if [ "$args" = '-xp' ];
then
    fileType=xp-tests;
else
    fileType=cy-tests;
fi

for d in ./*/$fileType;
do
    echo $d
    cd $d;
    ${HOME}/nmrfxstructure/target/structure-10.2.23-bin/structure-10.2.23/nmrfxstructure gen -s 1 project.yaml;
    cd $cwd;
done
