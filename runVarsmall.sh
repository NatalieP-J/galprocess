#!/bin/bash
#PBS -l nodes=1:ppn=1
#PBS -q workq
#PBS -l walltime=48:00:00
#PBS -N  NGC1600_2
cd $PBS_O_WORKDIR
module load python/2.7.6
export PYTHONPATH=$PATH:/mnt/scratch-lustre/njones/pyrate
python Varrateget.py 8
