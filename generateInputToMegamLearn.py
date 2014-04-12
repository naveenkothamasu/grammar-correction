#!/usr/bin/env python
import sys;
import nltk;

inputFile = open("../enwikinews-20140410-pages-articles-multistream.xml", "r");

model_its = open("input_its.train", "w");
model_your = open("input_your.train", "w");
model_their = open("input_their.train", "w");
model_lose = open("input_lose.train", "w");
model_to = open("input_to.train", "w");

for line in inputFile:
        tokenized = nltk.word_tokenize(line);
        tagged = nltk.pos_tag(tokenized)
        i = -1;
        for tup in tagged:
                i += 1;
                maxLen = len(tagged);
                if tup[0] == "to":
                        if i > 1 and i+2 < maxLen:
                                model_to.write(tup[0]+"\t p:"+tagged[i-1][1]+"\t p2:"+tagged[i-2][1]+"\t n:"+tagged[i+1][1]+"\t n2:"+tagged[i+2][1]);
                                model_to.write("\n");
                if tup[0] == "too":
                        if i > 1 and i+2 < maxLen:
                                model_to.write(tup[0]+"\t p:"+tagged[i-1][1]+"\t p2:"+tagged[i-2][1]+"\t n:"+tagged[i+1][1]+"\t n2:"+tagged[i+2][1])
                                model_to.write("\n");
                if tup[0] == "loose":
                        if i > 1 and i+2 < maxLen:
                                model_lose.write(tup[0]+"\t p:"+tagged[i-1][1]+"\t p2:"+tagged[i-2][1]+"\t n:"+tagged[i+1][1]+"\t n2:"+tagged[i+2][1])
                                model_lose.write("\n");
                if tup[0] == "lose":
                        if i > 1 and i+2 < maxLen:
                                model_lose.write(tup[0]+"\t p:"+tagged[i-1][1]+"\t p2:"+tagged[i-2][1]+"\t n:"+tagged[i+1][1]+"\t n2:"+tagged[i+2][1]);                                model_lose.write("\n");
                if tup[0] == "its":
                        if i > 1 and i+2 < maxLen:
                                model_its.write(tup[0]+"\t p:"+tagged[i-1][1]+"\t p2:"+tagged[i-2][1]+"\t n:"+tagged[i+1][1]+"\t n2:"+tagged[i+2][1]);
                                model_its.write("\n");
                if tup[0] == "it's":
                        if i > 1 and i+2 < maxLen:
                                model_its.write(tup[0]+"\t p:"+tagged[i-1][1]+"\t p2:"+tagged[i-2][1]+"\t n:"+tagged[i+1][1]+"\t n2:"+tagged[i+2][1]);
                                model_its.write("\n");
                if (tup[0] == "it" and i+1 < maxLen and tagged[i+1][0] == "is"):
                        if i > 1 and i+3 < maxLen:
                                model_its.write("it's\t p:"+tagged[i-1][1]+"\t p2:"+tagged[i-2][1]+"\t n:"+tagged[i+2][1]+"\t n2:"+tagged[i+3][1]);
                                model_its.write("\n");
                if tup[0] == "your":
                        if i > 1 and i+2 < maxLen:
                                model_your.write(tup[0]+"\t p:"+tagged[i-1][1]+"\t p2:"+tagged[i-2][1]+"\t n:"+tagged[i+1][1]+"\t n2:"+tagged[i+2][1]);
                                model_your.write("\n");
                if tup[0] == "their":
                        if i > 1 and i+2 < maxLen:
                                model_their.write(tup[0]+"\t p:"+tagged[i-1][1]+"\t p2:"+tagged[i-2][1]+"\t n:"+tagged[i+1][1]+"\t n2:"+tagged[i+2][1]);
                                model_their.write("\n");
                if tup[0] == "they're":
                        if i > 1 and i+2 < maxLen:
                                model_their.write(tup[0]+"\t p:"+tagged[i-1][1]+"\t p2:"+tagged[i-2][1]+"\t n:"+tagged[i+1][1]+"\t n2:"+tagged[i+2][1]);
                                model_their.write("\n");
                if(tup[0] == "they" and i+1 < maxLen and tagged[i+1][0] == "are"):
                        if i > 1 and i+3 < maxLen:
                                model_their.write("they're\t p:"+tagged[i-1][1]+"\t p2:"+tagged[i-2][1]+"\t n:"+tagged[i+2][1]+"\t n2:"+tagged[i+3][1]);
                                model_their.write("\n");
                if tup[0] == "you're":
                        if i > 1 and i+2 < maxLen:
                                model_your.write(tup[0]+"\t p:"+tagged[i-1][1]+"\t p2:"+tagged[i-2][1]+"\t n:"+tagged[i+1][1]+"\t n2:"+tagged[i+2][1]);
                                model_your.write("\n");
                if (tup[0] == "you" and i+1 < maxLen and tagged[i+1][0] == "are"):
                        if i > 1 and i+3 < maxLen:
                                model_your.write("you're\t p:"+tagged[i-1][1]+"\t p2:"+tagged[i-2][1]+"\t n:"+tagged[i+2][1]+"\t n2:"+tagged[i+3][1]);
                                model_your.write("\n");

inputFile.close();
model_its.close();
model_your.close();
model_their.close();
model_lose.close();
model_to.close();
