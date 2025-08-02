# Автор: М. Ишимов

from ipaddress import *
k = 0
network = ip_network(f'90.65.32.0/255.255.224.0')
for ip in network:
   if f'{ip:b}'.count('1') == f'{ip:b}'.count('0'):
        k += 1
print(k)
