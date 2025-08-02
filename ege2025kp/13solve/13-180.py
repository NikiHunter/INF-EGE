# Автор: М. Ишимов

from ipaddress import *
k = 0
network = ip_network(f'98.116.0.0/255.252.0.0')
for ip in network:
   if f'{ip:b}'.count('0') % 2 == 0:
        k += 1
print(k)





