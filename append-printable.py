#!/usr/bin/python3

import string
import sys

infile = open(sys.argv[1])
outfile = open(sys.argv[2],'w+')

for line in infile:
    for char in string.printable:
        outfile.write(char+line)

infile.close()
outfile.close()

