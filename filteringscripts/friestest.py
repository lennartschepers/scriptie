#!/usr/bin/env python3

import sys

with open(sys.argv[1], 'r') as f:
    with open(sys.argv[2], 'w+') as f1:
            for line in f:
                    line = line.split('\t')
                    f1.write(line[1])
                    f1.write('\n')
    
