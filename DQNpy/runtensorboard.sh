#!/bin/sh
if [ "$1" = "-p" ] && [ -n "$2" ]; then 
       echo "ture"
       basepath=$(cd `dirname $0`; pwd)
       echo $basepath
       tensorboard --logdir=$basepath/experiments/Breakout-v0/summaries_q_estimator --port "$2"
else 
       echo "[Please run shell]: "$0" -p [8888]"
fi
