#!/bin/bash

for((i=0;i<50;i++));
do
python rewriteVarsmall.py $i;
qsub runVarsmall.sh;
done
