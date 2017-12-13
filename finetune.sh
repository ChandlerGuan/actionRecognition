#!/bin/bash
LOG=/home/tracking/work/src/action/log/train-`date +%m-%d-%H-%M`.log
/home/tracking/work/git/caffe/build/tools/caffe train -solver action_solver.pt -weights /home/tracking/work/git/caffe/models/alexnet_chandler/bvlc_alexnet.caffemodel -gpu 0 2>&1 | tee $LOG
