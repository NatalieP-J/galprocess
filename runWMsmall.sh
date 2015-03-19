#!/bin/bash
#PBS -l nodes=1:ppn=1
#PBS -q workq
#PBS -l walltime=48:00:00
#PBS -N  NGC4552
cd $PBS_O_WORKDIR
module load python/2.7.6
export PYTHONPATH=$PATH:/mnt/scratch-lustre/njones/pyrate
python WMrateget.py 49
 0 1 2 3 4 5 6 7 8  49
