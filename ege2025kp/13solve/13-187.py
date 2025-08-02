# Автор: М. Ишимов

from ipaddress import *
res = []
network = ip_network(f'204.252.0.0/255.255.0.0')
for ip in network:
    res.append( f'{ip:b}'.count('1') )
print(max(res))
