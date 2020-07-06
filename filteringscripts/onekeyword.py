#!/usr/bin/env python3
from collections import defaultdict
import sys

keywords = []
with open('twitterscraper/groningenuseful', 'r') as keywordsfile:
    for line in keywordsfile:
        line = line.strip('\n')
        keywords.append(line)

onekwlist = []
with open(sys.argv[1], 'r') as f2:
    for line in f2:
        linelist = line.strip().split(' ')
        for word in linelist:
            if word in keywords:
                onekwlist.append(line.strip())
                break

with open('twitterscraper/corpus/twittercorpusvalidated1w', 'w+') as f3:
    for i in onekwlist:
        f3.write(i)
        f3.write('\n')


