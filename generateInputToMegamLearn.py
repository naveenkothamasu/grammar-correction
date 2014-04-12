#!/usr/bin/env python
import sys;
import nltk;

inputFile = open("../enwikinews-20140410-pages-articles-multistream.xml", "r");

model_its = open("input_its.train", "w");
model_your = open("input_your.train", "w");
model_their = open("input_their.train", "w");
model_lose = open("input_lose.train", "w");
model_to = open("input_to.train", "w");

def getFileName(token):
	if "it" in token:
		return model_its;
	if "you" in token:
		return model_your;
	if "the" in token:
		return model_their;
	if "lo" in token:
		return model_lose;
	if "to" in token:
		return model_to;

for line in inputFile:
        tokenized = nltk.word_tokenize(line);
        tagged = nltk.pos_tag(tokenized)
        i = -1;
        for tup in tagged:
                i += 1;
                maxLen = len(tagged);
                if tup[0] == "to" or tup[0] == "too" or tup[0] == "loose" or tup[0] == "lose" or tup[0] == "its" or tup[0] == "it's" or tup[0] == "your" or tup[0] == "you're" or tup[0] == "their" or tup[0] == "they're":
			f = getFileName(tup[0]);
                        if i > 1 and i+2 < maxLen:
                                f.write(tup[0]+"\t p:"+tagged[i-1][1]+"\t p2:"+tagged[i-2][1]+"\t n:"+tagged[i+1][1]+"\t n2:"+tagged[i+2][1]);
			elif i == 0:
                                f.write(tup[0]+"\t n:"+tagged[i+1][1]+"\t n2:"+tagged[i+2][1]);
			elif i == 1:
                                f.write(tup[0]+"\t p:"+tagged[i-1][1]+"\t n:"+tagged[i+1][1]+"\t n2:"+tagged[i+2][1]);
			elif i+1 < maxLen:
                                f.write(tup[0]+"\t p:"+tagged[i-1][1]+"\t p2:"+tagged[i-2][1]+"\t n:"+tagged[i+1][1]);
			else:
                                f.write(tup[0]+"\t p:"+tagged[i-1][1]+"\t p2:"+tagged[i-2][1]);
                        f.write("\n");
                elif (tup[0] == "it" and i+1 < maxLen and tagged[i+1][0] == "is"):
                        if i > 1 and i+3 < maxLen:
                                f.write("it's\t p:"+tagged[i-1][1]+"\t p2:"+tagged[i-2][1]+"\t n:"+tagged[i+2][1]+"\t n2:"+tagged[i+3][1]);
                                f.write("\n");
		elif (tup[0] == "they" and i+1 < maxLen and tagged[i+1][0] == "are"):
                        if i > 1 and i+3 < maxLen:
                                f.write("they're\t p:"+tagged[i-1][1]+"\t p2:"+tagged[i-2][1]+"\t n:"+tagged[i+2][1]+"\t n2:"+tagged[i+3][1]);
                                f.write("\n");
		elif (tup[0] == "you" and i+1 < maxLen and tagged[i+1][0] == "are"):
                                f.write("you're\t p:"+tagged[i-1][1]+"\t p2:"+tagged[i-2][1]+"\t n:"+tagged[i+2][1]+"\t n2:"+tagged[i+3][1]);
                                f.write("\n");

inputFile.close();
model_its.close();
model_your.close();
model_their.close();
model_lose.close();
model_to.close();
