#!/usr/bin/python3

import sys

infile = open(sys.argv[1])
outfile = open(sys.argv[2],'w+')
for line in infile:
    valid = False
    for character in line:
        if character.isupper():
            valid = True
    if valid:
        outfile.write(line)


infile.close()
outfile.close()
