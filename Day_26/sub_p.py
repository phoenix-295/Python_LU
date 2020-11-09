import subprocess as sp
import os


a = sp.Popen(['ping', '-n', '2', 'google.com'], stdout=sp.PIPE)

data = a.communicate()

print(data)
