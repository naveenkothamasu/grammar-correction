#!/usr/bin/env python
import sys;
import nltk;

inputFile = open("../hw3/hw3.dev.err.txt","r");

input_its = open("input_its.test", "w");
input_your = open("input_your.test", "w");
input_their = open("input_their.test", "w");
input_lose = open("input_lose.test", "w");
input_to = open("input_to.test", "w");

def getFileName(token):
        if "to" in token:
                return input_to;
        if "you" in token:
                return input_your;
        if "the" in token:
                return input_their;
        if "it" in token:
                return input_its;
        if "lo" in token:
                return input_lose;


for line in inputFile:
        tokenized = nltk.word_tokenize(line);
        tagged = nltk.pos_tag(tokenized)
        i = -1;
        for tup in tagged:
                i += 1;
                maxLen = len(tagged);
                if tup[0] == "to" or tup[0] == "too" or tup[0] == "loose" or tup[0] == "lose" or tup[0] == "its" or tup[0] == "it's" or tup[0] == "your" or tup[0] == "their" or tup[0] == "they're" or tup[0] == "you're":
                        f = getFileName(tup[0]);
                        if i > 1 and i+2 < maxLen:
                                f.write("?\t p:"+tagged[i-1][1]+"\t p2:"+tagged[i-2][1]+"\t n:"+tagged[i+1][1]+"\t n2:"+tagged[i+2][1]);
                        elif i == 0:
                                f.write("?\t n:"+tagged[i+1][1]+"\t n2:"+tagged[i+2][1]);
                        elif i == 1:
                                f.write("?\t p:"+tagged[i-1][1]+"n:"+tagged[i+1][1]+"\t n2:"+tagged[i+2][1]);
                        elif i+1 < maxLen:
                                f.write("?\t p:"+tagged[i-1][1]+"\t p2:"+tagged[i-2][1]+"\t n:"+tagged[i+1][1]);
                        else:
                                f.write("?\t p:"+tagged[i-1][1]+"\t p2:"+tagged[i-2][1]);
                        input_to.write("\n");
inputFile.close();
input_its.close();
input_your.close();
input_their.close();
input_lose.close();
input_to.close();
