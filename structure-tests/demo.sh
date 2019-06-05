#!/bin/bash

# Run this program from the following directory: ${HOME}/structure-supplements/structure-tests
# This script serves as a demo script for new users with
# machines that run BASH. The purpose of this script is to 
# run all tests we've been using to replenish nmrfxstructure.

# There are 5 RNA structures and 12 protein structures, each in its own directory
# labeled using the PDB ID tag. This script allows you to specify whether you want to run a batch
# of structures or a single structure and places nmrfxstructure output information for a structure
# in a directory called 'data'. To evaluate the standard output, or standard error, of each
# calculation, you can refer to the summary.log file in this directory. You can also refer to the 
# output information in the data directory. 

# IMPORTANT NOTE:

# If running a batch remotely, the 'runremote.sh' should be placed in home directory.



mode=$1

# Initializations depending on the mode...
if [[ $mode == 'gen' ]]; then
    seed=1;
elif [[ $mode == 'batch' ]]; then
    NSTRUCS=$2
    NKEEP=$3
    NPROC=$4
    if [[ -z $NSTRUCS ]] || [[ -z $NKEEP ]] || [[ -z $NPROC ]]; then
        echo 'Error: To calculate batch, need arguments 2=nStrucs, 3=nKeep, 4=nProcess'
        exit 1
    fi
    read -p 'REMOTE MACHINE? (y/n) : ' reply
    if [[ $reply == 'n' ]]; then
        echo "Running in ${USER}@`hostname`"
    elif [[ $reply == 'y' ]]; then
       read -p 'Enter remote user/host name (i.e. usr1@host): ' HOST
       if [[ -n $HOST ]]; then
           usrInfo=`ssh $HOST grep ${USER} /etc/passwd`
           if [[ -z $usrInfo ]]; then
               echo 'Credentials invalid.'
               exit 1
           else
               echo 'Hope you have an ssh key!'
           fi
       fi
    else
       echo 'Invalid entry.'
       exit 1
    fi
else
    echo 'Error: Specify mode as 1st argument.'
    echo 'Example: ' 
    echo '"./demo.sh batch" (batch of structures)'
    echo '"./demo.sh gen" (single structure)'
    exit 1
fi

trap ctrl_c INT

function ctrl_c() {
   echo "** DEMO CTRL-C exit **"
   exit 1
}


cwd=`pwd`;

rm -rf ./data summary.log;
mkdir -p data;

echo 'Performing calculations ...';

# master for-loop
for d in ./structures/*/*-tests;
do
    # Grabbing PDB ID and type of test to run
    struc=`echo $d | grep -o "[1-9][a-z0-9]*"`; # PDB ID
    strucType=`echo $d | grep -o "[a-z]*-tests"`; # type of test: xplor, cyana, nef (format: [type to test]-tests)
    # Making a directory to store output information. 
    mkdir -p  $cwd/data/$struc/$strucType;

    # Checking if mode for nmrfxs is 'gen' or 'batch'...
    if [[ $mode == 'gen' ]]; then
        # start of gen-if
        cd $d;
        seedNum=`echo seed*.txt | grep -o '[0-9]*'`;
        if [[ -n $seedNum ]]; then
            seed=`echo $seedNum`;
        fi
        echo -e "\n$d" >> $cwd/summary.log;
        nmrfxs gen -s $seed  project.yaml >>$cwd/summary.log 2>&1;
        if [ $? -eq 0 ]; then
            infoLine=`grep -o "Irp.*Dih.*Distance.*Total.*" output/temp${seed}.txt`;
        else
            printf "%15s %s\n" $struc/$strucType ': Failed Calculation!';
            cd $cwd;
            continue
        fi
        rm -rf $cwd/data/$struc/$strucType/output;
        mv ./output/* $cwd/data/$struc/$strucType/;
        rmdir ./output;
        cd $cwd; 
        # end of gen-if
    elif [[ $mode == 'batch' ]]; then
        if [[ -n $HOST ]]; then
            ../tools/shellscripts/runlocal.sh $HOST $d $strucType $struc $NSTRUCS $NKEEP $NPROC
            # if runlocal doesnt return 0, then we exit
            if [[ $? -ne 0 ]]; then
                #rm -rf ./data
                exit 1
            fi
        else
            cd $d
            nmrfxs batch -n $NSTRUCS -k $NKEEP -p $NPROC -a project.yaml > /dev/null
            mv ./output/* ./final/* $cwd/data/$struc/$strucType/;
            rmdir ./output ./final;
            cd $cwd;
        fi

        # Looking for summary.txt file
        summaryTxt=./data/${struc}/${strucType}/summary.txt
        if [[ -e "$summaryTxt" ]] && [[ -s "$summaryTxt" ]]; then
            infoLine=`cat $summaryTxt | head -n 1`;
        else
            printf "%15s %s\n" $struc/$strucType ': Failed Calculation!';
            cd $cwd;
            continue
        fi

    fi
    # checking if infoLine is not empty
    if [ -n "$infoLine" ]; then
        printf "%15s %s\n" $struc/$strucType ": $infoLine" ;
    else
        printf "%15s %s\n" $struc/$strucType ': Could not retrieve summary line';
        cd $cwd;
        continue
    fi
done

exit 0
