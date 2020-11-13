import socket

# Get Local Machine Name
print(socket.gethostname())

# Get Own Ip
print(socket.gethostbyname(socket.gethostname()))

# Full Qualified Domain name
print(socket.getfqdn('facebook.com'))

# Get Multiple ip if any
print(socket.gethostbyname_ex('facebook.com'))

# Get single ip
print(socket.gethostbyname('facebook.com'))
