import socket
# host = '192.168.76.127'
host = '127.0.0.1'
port = 1234
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((host, port))
s.listen(2)

client_socket, addr = s.accept()

print(addr, "  -->connected")
data1 = client_socket.recv(1024)
print("From Client :", data1)
d = int(data1.decode())
d = d**2

client_socket.send(str(d).encode())
client_socket.close()
s.close()
