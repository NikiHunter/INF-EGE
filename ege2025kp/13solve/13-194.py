# Автор: М. Ишимов

from ipaddress import *
k = 0
network = ip_network(f'186.135.80.0/255.255.252.0')
for ip in network:
    if f'{ip:b}'[:16].count('1') > f'{ip:b}'[16:].count('1'):
        k += 1
print(k)
