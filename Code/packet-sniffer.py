#!/usr/bin/python
#
# Simplest Form Of Packet sniffer in python
# Works On Linux Platform 
 
#import module
import socket 
import struct
import binascii
import os
import pye
import time

#os.remove("out_tcp.txt")
#os.remove("out_ip.txt")
os.remove("out.txt")
f1=open("out.txt", "w+")
#f2=open("out_ip.txt", "w+")

s=socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.ntohs(0x0800))

#while True:

t_end = time.time() + 60 * 1
while time.time() < t_end:

    # Capture packets from network
    pkt=s.recvfrom(65535)

    # extract packets with the help of pye.unpack class 
    unpack=pye.unpack()

    print "\n\n=========[+] ------------ Ethernet Header------ [+]"

    # print data on terminal
    with open('out.txt', 'a') as f1:
        for i in unpack.eth_header(pkt[0][0:14]).iteritems():
            a,b=i
            print >> f1, "{} :{}".format(a,b)
            print "{} : {} | ".format(a,b),
        print >> f1, '\n'
    print "\n===========[+] ------------ IP Header ------------[+]"
    with open('out.txt', 'a') as f1:
	#print >> f2,"IP Header\n"	
        for i in unpack.ip_header(pkt[0][14:34]).iteritems():
            a,b=i
            print >> f1, "{} :{}".format(a,b)
            print "{} : {} | ".format(a,b),
    	print >> f1, '\n'
    print "\n===========[+] ------------ Tcp Header -----------[+]"
    with open('out.txt', 'a') as f1:
	#print >> f,"TCP Header\n"
        for  i in unpack.tcp_header(pkt[0][34:54]).iteritems():
            a,b=i
            print >> f1, "{} :{}".format(a,b)
            print "{} : {} | ".format(a,b),
    	print >> f1, '\n'
