#！/usr/bin/env python3
import socket

# 建立 UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 連接到本地端的 UDP Server，port 為 20213
server_address = ("127.0.0.1", 20213)
sock.connect(server_address)

# 將訊息轉為 binary
message = b"This is a test from python client"

# 送出訊息
sock.sendall(message)

# 接收回應訊息
data, address = sock.recvfrom(1024)

# 將 binary 轉回文字
message = data.decode("utf-8")

# 印出回應訊息
print(message)

# 關閉連線
sock.close()
