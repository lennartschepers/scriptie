#!/usr/bin/env python3

#remove duplicates if they are adjacent

import sys
from itertools import groupby

# open input file 

with open(sys.argv[1], 'r') as f:
    filelist = f.readlines()

with open(sys.argv[2], 'w+') as f1:
    for i in groupby(filelist):
        i = i[0].rstrip()
        f1.write(i)
        f1.write('\n')

