#!/usr/bin/python3

#regex.py <input> <output>

#finds all ip addresses in input file

import re
import sys
octet = "[0-9]{1,3}\."
end = "[0-9]{1,3}"
pattern = re.compile(octet+octet+octet+end)
with open(sys.argv[2],'w+') as outFile:
    with open(sys.argv[1],'r') as file:
        for line in file:
            info = re.findall(pattern,line)
            for item in info:
                outFile.write(str(item)+'\n')
