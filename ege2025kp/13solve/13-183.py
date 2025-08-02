# Автор: М. Ишимов

from ipaddress import *
k = 0
network = ip_network(f'99.64.0.0/255.192.0.0')
for ip in network:
   if f'{ip:b}'[-2:] == '11':
        k += 1
print(k)
