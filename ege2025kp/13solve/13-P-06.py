from ipaddress import *
net = ip_network('217.8.244.3/255.255.252.0',0)
for ip in net:
    print(ip)
    break
