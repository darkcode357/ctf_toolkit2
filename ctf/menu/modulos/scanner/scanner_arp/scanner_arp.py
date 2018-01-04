#! /usr/bin/python

# Author == @avicoder

import sys, getopt

r = '\033[31m'  # red
b = '\033[34m'  # blue
g = '\033[32m'  # green
y = '\033[33m'  # yellow
m = '\033[34m'  # magenta
c = '\033[36m'  # cyan


def scan_arp():
    import sys
    import scapy.all
    ip = input("ranger =>")
    try:
        alive, dead = srp(Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=ip), timeout=2, verbose=0)
        print ("MAC - IP")
        for i in range(0, len(alive)):
            print (alive[i][1].hwsrc + " - " + alive[i][1].psrc)
    except:
        pass
scan_arp()