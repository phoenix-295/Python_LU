import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# server_1 = '192.168.76.127'
server_1 = '127.0.0.1'
port1 = 1234


s.connect((server_1, port1))
s.send("2".encode())
msg = s.recv(1024)
print(msg)
s.close()
