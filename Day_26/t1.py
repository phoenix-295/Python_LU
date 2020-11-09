import subprocess as sp
import os
import signal
import sys
import time


def signal_handler(signal, frame):
    sys.exit(0)


child = sp.Popen(['ping', '-n', '50', 'google.com'], stdout=sp.PIPE)
time.sleep(5)
# child.terminate()
signal.signal(signal.SIGINT, signal_handler)
data = child.communicate()[0].decode()


print(data)
