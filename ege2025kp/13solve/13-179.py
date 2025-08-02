# Автор: М. Ишимов

from ipaddress import *
k = 0
network = ip_network(f'213.0.0.0/255.192.0.0')
for ip in network:
   if '111' in f'{ip:b}':
        k += 1
print(k)




