rm -rf ~/work/git/caffe/data/actionTrain
build/tools/convert_imageset --shuffle --resize_height=256 --resize_width=256 ~/work/src/action/dataset/ ~/work/src/action/actionTrain.txt  ~/work/git/caffe/data/actionTrain
/home/tracking/work/git/caffe/build/tools/compute_image_mean /home/tracking/work/git/caffe/data/actionTrain /home/tracking/work/git/caffe/data/actionTrain/trainMean.binaryproto
