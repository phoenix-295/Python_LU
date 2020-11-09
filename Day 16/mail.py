import re
import requests

mail12 = "marvel.iorn-man_3000@1337days.com"

url = "http://csed.thapar.edu/faculty"

r = requests.get(url)

data = r.text

email = r"[a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+"

listmail = re.findall(email, url)

for each in listmail:
    print(each)
