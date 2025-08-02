# Автор: М. Ишимов

from ipaddress import *
k = 0
network = ip_network(f'174.114.120.0/255.255.252.0')
for ip in network:
   if f'{ip:b}'.count('1') % 2 == 0:
        k += 1
print(k)
