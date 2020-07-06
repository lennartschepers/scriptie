#!/usr/bin/env python3
from collections import defaultdict
import sys

keywords = set()
with open('fries', 'r') as keywordsfile:
    for line in keywordsfile:
        line = line.strip('\n')
        keywords.add(line)


with open(sys.argv[1], 'r') as f2:
    twokeywords = 0
    corpuslist = list()
    for line in f2:
        line = line.lower()
        splitline = line.split(' ')
        # look if at least two different words in the line are in the keywordlist
        lineset = set(line.split())
        if len(lineset.intersection(keywords)) >= 5:
            corpuslist.append(line)


with open(sys.argv[2], 'w+') as f3:
    for i in corpuslist:
        f3.write(str(i))
