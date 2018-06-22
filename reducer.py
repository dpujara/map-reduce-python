#!/usr/bin/python
from operator import itemgetter
from collections import defaultdict
import sys

word2count = {}
l = []
# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    word = line.split('\t')
    if(len(word)==2):
        if(word[0] in word2count):
            word2count[word[0]].append(word[1]) 

        else:
            word2count[word[0]] = [word[1]]
#            print(word2count)
# do not forget to output the last word if needed!
for word in word2count.keys():
    print '%s\t%s' % (word,word2count[word])
