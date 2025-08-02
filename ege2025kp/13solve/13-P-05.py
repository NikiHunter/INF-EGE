from ipaddress import *
net = ip_network('10.8.248.131/255.255.224.0',0)
for ip in net:
    print(ip)
    break
