#!/bin/bash

for((i=0;i<50;i++));
do
python rewriteWMGensmall.py $i;
qsub runWMGensmall.sh;
done
