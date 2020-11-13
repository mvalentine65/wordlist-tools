#! /usr/bin/python3
import sys # allows access command line args and exit()
from scapy.all import rdpcap # module for manipulating pcaps

if len(sys.argv) != 3: # check for input and output files
    print("\nUsage: %s <input file> <output file>\n" % (sys.argv[0])) # printf
    sys.exit(1) # exit program after printing help message

start = sys.argv[1] # assigns args to variables
end = sys.argv[2]
data = "" # need this to append data to later

packets = rdpcap(start) # scapy function to parse pcap files

for packet in packets: # scan all packets for data
    if hasattr(packet,'load'): # if the selected packet has a data payload
        if len(packet.load) == 1: # if the length of the data is one byte
            data += str(packet.load)[2]  # add the byte to the extracted bytes
print(data) # display the extracted bytes on screen

#print would be bad for large files but I already know this isnt too big

