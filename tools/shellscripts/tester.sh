#!/bin/bash

pdbFile="pdbModel1.pdb"

echo ".... Running Structures ...."

for d in ./*/;
do
cd  $d;
echo $d;
mv ../../pythonscripts/testdis.py .;
mv ../../pythonscripts/getFiles.py .;

python getFiles.py distances.lol;
python getFiles.py distances.upl;

for f in ambi_const_file.*;
do
	if [ ${f: -4} == ".lol"  ];
	then
		${HOME}/nmrfxstructure/target/structure-10.2.9-bin/structure-10.2.9/nmrfxstructure testdis.py $pdbFile $f;
		cp test_distances.lol ./readyTestDistances.lol;
		cat testDisOutput.lol >> readyTestDistances.lol;
	else
		${HOME}/nmrfxstructure/target/structure-10.2.9-bin/structure-10.2.9/nmrfxstructure testdis.py $pdbFile $f;
		cp test_distances.upl ./readyTestDistances.upl
		cat testDisOutput.upl >> readyTestDistances.upl
                #python ../removeDup.py Test_distances.upl
	fi
done

${HOME}/nmrfxstructure/target/structure-10.2.9-bin/structure-10.2.9/nmrfxstructure batch -n 100 -k 20 -p 12 -a project.yaml

mv testdis.py ../../pythonscripts;
mv getFiles.py ../../pythonscripts;
cd ..;
done
