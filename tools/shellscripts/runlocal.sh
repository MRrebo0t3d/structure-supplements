trap ctrl_c SIGINT

function ctrl_c() {
   echo "** RUNLOCAL CTRL-C exit **"
   ssh -t ${REMOTE_MACHINE} exit
   exit
}

# Input Args
HOMEDIR=${HOME} # should be the same for remote home (EX: /home/tedcolon)
REMOTE_MACHINE=$1 # tedcolon@ucsbj1
localProj=$2 # ex: ./rnastrucs/2koc/xp-tests : [project.yaml, input/]
remoteProj=${HOMEDIR}/testprojs # ex: /home/tedcolon/testprojs/
TEST=$3 #  ex: xp-tests
STRUC=$4 # ex: 2koc
NSTRUCS=$5
NKEEP=$6
NPROC=$7

ssh ${REMOTE_MACHINE} "mkdir -p ${remoteProj}"
scp -r -p -q ${localProj}/ ${REMOTE_MACHINE}:${remoteProj}

ssh ${REMOTE_MACHINE} "${HOMEDIR}/runremote.sh ${remoteProj} ${TEST} $STRUC $NSTRUCS $NKEEP $NPROC"
if [[ $? -eq 0 ]]; then 
    scp -r -p -q ${REMOTE_MACHINE}:${remoteProj}/${STRUC}/${TEST}/\{final,output\}/* ./data/${STRUC}/${TEST}
else
   echo 'ERROR ssh returned a nonzero exit status.'
   exit 1
fi
