#!/bin/bash

for d in 2koc 2l1v 2l5z 2lu0 2m24; do
    cd $d;
    echo =====;
    echo pwd;
    echo =====;
    sed -i '$ a \    swap : 20\' cy_tests/project.yaml;
    sed -i '$ a \    swap : 20\' xp_tests/project.yaml;
    cd ..;
    cat $d/*tests/project.yaml;
done
