#!/usr/bin/env python3

# script that filters most frisian tweets out of a gronings dataset, also a few terms to filter out most scandinavian tweets

import sys

fries = {'frysk','fryslân', 'fryske', 'boppe','gjin','omrop','hei','rêst', '(frysk)','friesland', 'sizze', 'yn','syn','hy','wêze','hawwe','hyt','wy','trije','troch','på', 'gå', 'ek', 'oer', 'fryslan', 'my', 'är','dy','dyn','it','sy', 'myn','yk','ikke','jag','jeg','harms', 'harmsen','disco', 'disko'}
foreignchars = {'ø'}
with open(sys.argv[1], 'r') as f:
    with open(sys.argv[2], 'w+') as f2:
        for line in f:
            line = line.lower()
            line = line.replace(',','')
            lineset = set(line.split())
            if len(lineset.intersection(fries)) < 1:
                charset = {i for i in line}
                if len(foreignchars.intersection(charset)) < 1:
                    f2.write(line)
