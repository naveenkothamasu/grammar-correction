#!/usr/bin/env python
import sys;
import nltk;

inputFile = open("../hw3/hw3.dev.err.txt","r");

input_its = open("input_its.test", "w");
input_your = open("input_your.test", "w");
input_their = open("input_their.test", "w");
input_lose = open("input_lose.test", "w");
input_to = open("input_to.test", "w");

for line in inputFile:
        tokenized = nltk.word_tokenize(line);
        tagged = nltk.pos_tag(tokenized)
        i = -1;
        for tup in tagged:
                i += 1;
                maxLen = len(tagged);
                if tup[0] == "to":
                        if i > 1 and i+2 < maxLen:
                                input_to.write("?\t p:"+tagged[i-1][1]+"\t p2:"+tagged[i-2][1]+"\t n:"+tagged[i+1][1]+"\t n2:"+tagged[i+2][1]);
                                input_to.write("\n");
                if tup[0] == "too":
                        if i > 1 and i+2 < maxLen:
                                input_to.write("?\t p:"+tagged[i-1][1]+"\t p2:"+tagged[i-2][1]+"\t n:"+tagged[i+1][1]+"\t n2:"+tagged[i+2][1])
                                input_to.write("\n");
                if tup[0] == "loose":
                        if i > 1 and i+2 < maxLen:
                                input_lose.write("?\t p:"+tagged[i-1][1]+"\t p2:"+tagged[i-2][1]+"\t n:"+tagged[i+1][1]+"\t n2:"+tagged[i+2][1])
                                input_lose.write("\n");
                if tup[0] == "lose":
                        if i > 1 and i+2 < maxLen:
                                input_lose.write("?\t p:"+tagged[i-1][1]+"\t p2:"+tagged[i-2][1]+"\t n:"+tagged[i+1][1]+"\t n2:"+tagged[i+2][1]);                                
                                input_lose.write("\n");
                if tup[0] == "its":
                        if i > 1 and i+2 < maxLen:
                                input_its.write("?\t p:"+tagged[i-1][1]+"\t p2:"+tagged[i-2][1]+"\t n:"+tagged[i+1][1]+"\t n2:"+tagged[i+2][1]);
                                input_its.write("\n");
                if tup[0] == "it's":
                        if i > 1 and i+2 < maxLen:
                                input_its.write("?\t p:"+tagged[i-1][1]+"\t p2:"+tagged[i-2][1]+"\t n:"+tagged[i+1][1]+"\t n2:"+tagged[i+2][1]);
                                input_its.write("\n");
                if (tup[0] == "it" and i+1 < maxLen and tagged[i+1][0] == "is"):
                        if i > 1 and i+3 < maxLen:
                                input_its.write("?\t p:"+tagged[i-1][1]+"\t p2:"+tagged[i-2][1]+"\t n:"+tagged[i+2][1]+"\t n2:"+tagged[i+3][1]);
                                input_its.write("\n");
                if tup[0] == "your":
                        if i > 1 and i+2 < maxLen:
                                input_your.write("?\t p:"+tagged[i-1][1]+"\t p2:"+tagged[i-2][1]+"\t n:"+tagged[i+1][1]+"\t n2:"+tagged[i+2][1]);
                                input_your.write("\n");
                if tup[0] == "their":
                        if i > 1 and i+2 < maxLen:
                                input_their.write("?\t p:"+tagged[i-1][1]+"\t p2:"+tagged[i-2][1]+"\t n:"+tagged[i+1][1]+"\t n2:"+tagged[i+2][1]);
                                input_their.write("\n");
                if tup[0] == "they're":
                        if i > 1 and i+2 < maxLen:
                                input_their.write("?\t p:"+tagged[i-1][1]+"\t p2:"+tagged[i-2][1]+"\t n:"+tagged[i+1][1]+"\t n2:"+tagged[i+2][1]);
                                input_their.write("\n");
                if(tup[0] == "they" and i+1 < maxLen and tagged[i+1][0] == "are"):
                        if i > 1 and i+3 < maxLen:
                                input_their.write("?\t p:"+tagged[i-1][1]+"\t p2:"+tagged[i-2][1]+"\t n:"+tagged[i+2][1]+"\t n2:"+tagged[i+3][1]);
                                input_their.write("\n");
                if tup[0] == "you're":
                        if i > 1 and i+2 < maxLen:
                                input_your.write("?\t p:"+tagged[i-1][1]+"\t p2:"+tagged[i-2][1]+"\t n:"+tagged[i+1][1]+"\t n2:"+tagged[i+2][1]);
                                input_your.write("\n");
                if (tup[0] == "you" and i+1 < maxLen and tagged[i+1][0] == "are"):
                        if i > 1 and i+3 < maxLen:
                                input_your.write("?\t p:"+tagged[i-1][1]+"\t p2:"+tagged[i-2][1]+"\t n:"+tagged[i+2][1]+"\t n2:"+tagged[i+3][1]);
                                input_your.write("\n");

inputFile.close();
input_its.close();
input_your.close();
input_their.close();
input_lose.close();
input_to.close();
