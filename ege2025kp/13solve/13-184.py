# Автор: М. Ишимов

from ipaddress import *
k = 0
network = ip_network(f'154.233.0.0/255.255.0.0')
for ip in network:
   if f'{ip:b}'[-1] == '0':
        k += 1
print(k)
