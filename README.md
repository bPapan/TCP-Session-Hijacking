# TCP-Session-Hijacking

In this project, I have tried to demonstrate how we can cause a TCP Session Hijacking attack in a network. We have three Virtual Machines (SEED: https://seedsecuritylabs.org/labsetup.html) in a network. First we will conduct ARP Spoofing attack from the attacker virtual machine. Then the attacker will try to get the session info of the open TCP connection from the other two machines. 

To run this:

1. Create three SEED (https://drive.google.com/file/d/138fqx0F8bThLm9ka8cnuxmrD6irtz_4m/view) virtual machines in the same network: victim client, attacker and server
2. Download and unzip the directory in one of the SEED VMs, this will be the attacker VM
3. Update the cmnd.sh file in the "Code" folder with the correct IP addresses of the client and the server in the attacker VM
4. Start the server by running echo-tcp-server.py (available in the SEED vm) file with a correct IP and port in the server VM
5. Start the client by running echo-tcp-client.py (available in the SEED vm) file in the a correct IP and port in the client VM
6. Run arp-spoof.py in the attacker VM
7. Check in the server and the client if the attack has been successful by running the arp -a command
8. Run Wireshark in the attacker VM to sniff the pakcets
9. Then run the ./cmnd.sh command in the attacker VM to launch the TCP Session hijacking attack
