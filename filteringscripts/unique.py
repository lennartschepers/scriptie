#!/usr/bin/env python3

import sys
from itertools import groupby

# open input file 

with open(sys.argv[1], 'r') as f:
    filelist = f.readlines()
tweetset = set()
for i in filelist:
    i = i.rstrip()
    tweetset.add(i)

with open(sys.argv[2], 'w+') as f1:
    for i in tweetset:
        f1.write(i)
        f1.write('\n')

