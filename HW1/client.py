#！/usr/bin/env python3
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("127.0.0.1", 20213))
msg = b"This is a test from python client"
s.send(msg)
data, address = s.recvfrom(1024)
rmsg = data.decode("utf-8")
print(rmsg)
s.close()