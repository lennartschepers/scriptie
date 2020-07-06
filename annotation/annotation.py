#!/usr/bin/env python3

import sys

sents = list()
with open(sys.argv[1], 'r') as f:
    for line in f:
        sents.append(line)


x = int(input('type the index number of where you want to resume'))
currentsents = sents[x:]
#f1 is 'containslang'. f2 is 'doesnotcontainlang'
with open(sys.argv[2], 'a+') as f1:
    with open(sys.argv[3], 'a+') as f2:
        for sent in currentsents:
            print(sent, sents.index(sent))
            n = input('num if lang, else enter nothing')
            try:
                n = int(n)
                f1.write(" ".join(sent.split()[n:]))
                f1.write('\n')

            except ValueError:
                f2.write(" ".join(sent.split()))
                f2.write('\n')
                

