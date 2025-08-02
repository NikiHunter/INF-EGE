# Автор: М. Ишимов

from ipaddress import *
res = []
network = ip_network(f'124.8.0.0/255.248.0.0')
for ip in network:
    res.append( f'{ip:b}'.count('0') )
print(max(res))
