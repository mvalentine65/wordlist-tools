#!/usr/bin/env python

from scapy.all import *
import base64


capture = rdpcap('first.pcap')
ping_data = ""

for packet in capture:
   # if packet[ICMP].type == 8:
    ping_data += packet.load[:10]

with open("test","w+") as file:
    file.write(ping_data)

