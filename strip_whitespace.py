#!/usr/bin/python3

#strips whitespace and punctuation
#outputs all alphanumeric characters

#python3 strip_whitespace.py <inputFile> <outputFile>

import sys
outfile = open(sys.argv[2],'w+')
with open(sys.argv[1]) as infile:
    for line in infile:
        line = line.strip().replace(' ','')
        line = ''.join(char for char in line if char.isalnum())
        outfile.write(line+'\n')
outfile.close()
