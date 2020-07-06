#!/usr/bin/env python3

import sys

x = set()
y = set()

#keywords
with open(sys.argv[2], 'r') as f1:
    for line in f1:
            line = line.rstrip()
            y.add(line)

with open(sys.argv[1], 'r') as f:
    for line in f:
        line = line.split()
        try:
            if line[0] in y:
                x.add(line[0])
        except:
            pass

print(len(x))
