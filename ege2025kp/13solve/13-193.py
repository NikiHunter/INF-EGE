# Автор: М. Ишимов

from ipaddress import *
k = 0
network = ip_network(f'154.24.165.32/255.255.255.224')
for ip in network:
    if f'{ip:b}'[:16].count('1') < f'{ip:b}'[16:].count('1'):
        k += 1
print(k)
