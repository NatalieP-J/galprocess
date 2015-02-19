#!/bin/bash

for((i=1;i<50;i++));
do
python rewriteWMsmall.py $i;
qsub runWMsmall.sh;
done
