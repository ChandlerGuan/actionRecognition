# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 20:23:12 2017

@author: chandler
"""
#import os
#
#def geneListfile():
#	trainPath = "train";
#	listFile = open('trainFilelist.txt', 'w');
#	for parent,dirnames,filenames in os.walk(trainPath): 
#		dirnames.sort();
#		for dirname in dirnames:
#			for subParent,subDirnames,subFilenames in os.walk(os.path.join(trainPath,dirname)):
#				subFilenames.sort();            
#				for filename in subFilenames:
#					listFile.write(os.path.join(dirname,filename)+' '+dirname[1]+'\n');	            
#	listFile.close();
#    
#if __name__ == "__main__":
#    geneListfile();

import os
import random

select_table = ['0','4','5','6','7','9','10','11','12','13']
#                0:normal 4:turn left 5:turn right 6:watch rearview
#                7:turn to back seat 9:smoke 10:drink 11:eat
#                12:phone call 13:watch telephone

dataset_path = "/home/tracking/work/src/action/dataset/"
list_file_path = '/home/tracking/work/src/action/'
test_split = 0.1;

if __name__ == "__main__":
    listFile = open(os.path.join(list_file_path,'action.txt'),'w')
    total_list = [];
    for folder_name in os.listdir(dataset_path):
        if (not folder_name in select_table):
            continue;
        for file_name in os.listdir(os.path.join(dataset_path,folder_name)):
            tmp_line = os.path.join(folder_name,file_name)+' '+str(select_table.index(folder_name))+'\n'
#            print(tmp_line)            
            listFile.write(tmp_line)
            total_list.append(tmp_line)
    listFile.close()
    
    random.shuffle(total_list)
    trainFile = open(os.path.join(list_file_path,'actionTrain.txt'),'w')
    testFile = open(os.path.join(list_file_path,'actionTest.txt'),'w')
    for i in range(int(test_split*len(total_list))):
        testFile.write(total_list[i])
    for i in range(int(test_split*len(total_list)),len(total_list)):
        trainFile.write(total_list[i])
    trainFile.close()
    testFile.close()
    
        