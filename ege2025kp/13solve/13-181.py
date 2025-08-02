# Автор: М. Ишимов

from ipaddress import *
k = 0
network = ip_network(f'250.135.101.80/255.255.255.248')
for ip in network:
   if f'{ip:b}'.count('0') % 3 == 0:
        k += 1
print(k)





