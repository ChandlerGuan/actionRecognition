rm -rf ~/work/git/caffe/data/actionTest
build/tools/convert_imageset --shuffle --resize_height=256 --resize_width=256 ~/work/src/action/dataset/ ~/work/src/action/actionTest.txt  ~/work/git/caffe/data/actionTest
