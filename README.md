# DenialOfService-Scripts
This repository contains several denial-of-service or DDOS scripts that can be used for penetration testing

1) Ping_of_death_flood.py : Usage: <target> <broadcast IP> <threads> 
  
 Ping of Death (a.k.a. PoD) is a type of Denial of Service (DoS) attack in which an attacker attempts to crash, destabilize, or freeze the targeted computer or service by sending malformed or oversized packets using a simple ping command.
 
2) udpflooder.py : Usage: udpflooder.py ip port(0=random) length(0=forever)

A UDP flood is a form of volumetric Denial-of-Service (DoS) attack where the attacker targets and overwhelms random ports on the host with IP packets containing User Datagram Protocol (UDP) packets.

3) pinger2.py : Usage: %s <Target IP> <Packet Size (MAX 65500)> <Duration Time (0 = forever)>
  
 An Internet Control Message Protocol (ICMP) flood attack, also known as a Ping flood attack, is a common Denial-of-Service (DoS) attack in which an attacker attempts to overwhelm a targeted device with ICMP echo-requests (pings).
