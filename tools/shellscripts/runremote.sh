#/bin/sh

# MACHINE: UCSBJ1
# INPUT ARGS
DIR=$1 # /home/tedcolon/testprojs
TEST=$2 # xp-tests
STRUC=$3 #2koc
NSTRUCS=$4 # 4
NKEEP=$5 # 2
NPROC=$6 # 4

# SETTING UP NMRFXS
#export NMRFX=${HOME}/structure-10.3.17 # *** depends on remote machine ***
#export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64/jre # *** depends on remote machine ***
#export PATH=${PATH}:${NMRFX}

#mkdir -p ${DIR}/${STRUC}
#if [[ ! -e "./testprojs/${STRUC}/${TEST}" ]] && [[ -e "./testprojs/${TEST}" ]]; then
#    mv ./testprojs/${TEST} ./testprojs/${STRUC}
#fi
#cd ${DIR}/${STRUC}/${TEST}

#nmrfxs batch -n $NSTRUCS -k $NKEEP -p $NPROC -a project.yaml;
