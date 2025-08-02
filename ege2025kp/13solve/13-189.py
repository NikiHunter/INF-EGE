# Автор: М. Ишимов

from ipaddress import *
res = []
network = ip_network(f'94.159.76.0/255.255.255.128')
for ip in network:
    res.append( f'{ip:b}'.count('0') )
print(min(res))
