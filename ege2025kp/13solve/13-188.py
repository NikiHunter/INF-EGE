# Автор: М. Ишимов

from ipaddress import *
res = []
network = ip_network(f'135.221.128.0/255.255.128.0')
for ip in network:
    res.append( f'{ip:b}'.count('1') )
print(min(res))
