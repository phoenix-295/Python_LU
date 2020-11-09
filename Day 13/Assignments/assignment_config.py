from configparser import ConfigParser
import socket
print(socket.gethostbyname_ex(socket.gethostname())[-1])

config = ConfigParser()
config.read("exc.ini")

current_path = config.get("EXT", "current_path")
from1 = config.get("EXT", "from")
to = config.get("EXT", "to")

print("Current Path :", current_path)
print("From :", from1)
print("To :", to)
