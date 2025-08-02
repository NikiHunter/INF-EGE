# Автор: М. Ишимов

from ipaddress import *
k = 0
network = ip_network(f'99.165.134.0/255.255.254.0')
for ip in network:
   if f'{ip:b}'.count('1') % 3 == 0:
        k += 1
print(k)

