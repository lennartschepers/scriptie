#!/usr/bin/env python3

import sys

linelist = []
with open(sys.argv[1], 'r') as file1:
    for line in file1:
            line = line.rstrip()
            line = line.replace(',', '')
            line = line + ",NED"
            linelist.append(line)


with open(sys.argv[2], 'w+') as file2:
    for i in linelist:
        file2.write(i)
        file2.write('\n')
            




