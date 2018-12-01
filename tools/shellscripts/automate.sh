#!/bin/bash

echo 'Printing statistical analysis...'

for d in ./*;
do
    if [ -d $d ];
    then
	cd $d;
        python ${HOME}/pythonscripts/molprobProcess.py;
	cd ..;
    fi
done
