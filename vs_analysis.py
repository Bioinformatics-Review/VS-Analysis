# Author: Dr. Muniba Faiza
# Copyright Muniba Faiza 2021



#!/usr/bin/env python

import os
import itertools
import collections
import pprint
import sys

mypath = os.path.abspath(os.getcwd())								#get path of current dir

print ("Directory path detected \n")

import os
import os.path
file_list = os.listdir(mypath)													#read all filenames in the dir


import glob
num_files = len(glob.glob1(mypath,"*log*.txt"))                       #collecting the total number of log files in the directory.
print('There are',num_files, 'log files in the current directory\n\n')

file_dict = {}																	# Create an empty dict

for file_name in file_list:

	import fnmatch
	if fnmatch.fnmatch(file_name, '*log*.txt'):
		with open(os.path.join(mypath, file_name), "r") as src_file:
			
			
			for line in src_file:
				if '-+' in line:													#looking for binding affinity table
					nextline = next(src_file)
					value = nextline[nextline.find("-")+0:].split()[0]					#split at '-' and print binding affinity including '-'
					file_dict[file_name] = value
				
from collections import OrderedDict
from operator import itemgetter

sorted_dict = OrderedDict(sorted(file_dict.items(), key=itemgetter(1), reverse=True))               #sorting binding affinities
print ("Binding affinities sorted \n\n")

n = eval(input("Enter the number of compounds for which you want to get binding affinities:\n"))

#checking if the user input is correct.
if n>num_files:
	print('Enter a valid number. The number you entered exceeds the total number of log files present in the current directory.\n\n')
	sys.exit()

with open("output.txt", "w") as f:
	
	firstnpairs = list(sorted_dict.items())[:n]							                                    #get first n elements from dict

	print('\n'.join("{}: {}".format(k, v) for k, v in firstnpairs), file=f)			                        #print results without quotes

print ("Done! The result is provided in the output.txt file.")
				
				









