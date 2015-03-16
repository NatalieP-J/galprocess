#!/bin/bash
#PBS -l nodes=1:ppn=1
#PBS -q workq
#PBS -l walltime=24:00:00
#PBS -N  NGC45522
cd $PBS_O_WORKDIR
module load python/2.7.6
export PYTHONPATH=$PATH:/mnt/scratch-lustre/njones/pyrate
python WMrateget.py 49
