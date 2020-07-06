#!/usr/bin/env python3

import sys

kwset = set()
with open(sys.argv[1],'r') as f:
    for line in f:
        kw = line.split()
        if len(kw) ==1:
            kwset.add(kw[0])


with open('groningenuseful', 'w+') as f2:
    for i in kwset:
        f2.write(i.strip())
        f2.write('\n')
