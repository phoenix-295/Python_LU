import os
a = os.popen("ping google.com")

data = a.read()


print(data)
