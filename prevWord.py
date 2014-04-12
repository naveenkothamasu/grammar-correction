#!/usr/bin/env python
import sys;
import re;

inputFile = open("/home/naveen/nltk_data/corpora/abc/rural.txt", "r");
#inputFile = open("temp.txt", "r");
outputFile = open("train.out", "w");
for line in inputFile:
	line = line.lower();
	for m in re.finditer("it's", line):
		end = m.start();
		if end == 0:
			print "START";
		else:
			prev = line[0:end-1];
			start = re.search(".+\s", prev);
			ne = re.search("\s", nextFrag);
			if start == None:
				print line[end-1:end];
			else:
				s1 = len(start.group(0));
				print prev[s1:end];
