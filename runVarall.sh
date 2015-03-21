#!/bin/bash

for((i=0;i<10;i++));
do
python rewriteVarsmall.py $i;
qsub runVarsmall.sh;
done
