#!/usr/bin/env python3

import sys

infile = open(sys.argv[1],'r')
outfile = open(sys.argv[2],'w+')
MIN_LENGTH = int(sys.argv[3])
MAX_LENGTH = int(sys.argv[4])

for line in infile:
    line = line.strip()
    if MIN_LENGTH <= len(line) <= MAX_LENGTH:
        outfile.write(line+"\n")

