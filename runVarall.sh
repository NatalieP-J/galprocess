#!/bin/bash

for((i=0;i<6;i++));
do
python rewriteVarsmall.py $i;
qsub runVarsmall.sh;
done
