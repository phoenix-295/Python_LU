import re
import requests

"172.16.55.13"
url = "https://study-ccna.com/classes-of-ip-addresses/"
r = requests.get(url)
data = r.text

# ip_con = r"[0-9]+\.+[0-9]+\.+[0-9]+\.+[0-9]"
ip_con = r"[0-9]+(?:\.[0-9]+){3}"
find_ip = re.findall(ip_con, data)

for each in find_ip:
    print(each)
