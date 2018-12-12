#!/bin/bash

# Initializing the input arguments
pyFile=$1;
specifiedMember=$2;

# Checking if an input file was provided
if [ -z "$1" ]
then
    echo 'Specify input file';
    exit 1;
fi

# naming an output file
oFile="${1%.*}_wo_imp"

# grabbing everything but the import statements and creating a new file
sed -nr '/.*import.*/!p' $pyFile > $oFile.py;

# Checking if a member was specified as the second input argument
if [ $# -eq 0 ];
then
    inpt=`echo $oFile+`;

else
    inpt=`echo "$oFile.$specifiedMember+"`;
fi

# running pydoc-markdown and saving output markdown file at docs directory
pydocmd simple $inpt > "./${1%.*}.md";

# removing excess files
rm $oFile.py *.pyc;

exit 0
