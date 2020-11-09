import os
import sys

list1 = ["fb.com", "google.com", "steam.com"]

if sys.platform == "win32":
    cmd = "ping -n 1 "
    match = "reply from"
elif sys.platform == "linux":
    cmd = "ping -c 1 "
    match = "byte from"

for d in list1:
    cmd1 = cmd + d
    resp = os.popen(cmd1)
    data = resp.read()

if "match" in data:
    print(d, ">>>is live")
else:
    print(d, ">>> is not live")
