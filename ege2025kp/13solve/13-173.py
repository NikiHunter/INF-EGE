# Автор: М. Ишимов

from ipaddress import *
ip = ip_address('190.120.251.78')
net = ip_address('190.120.251.0')
for mask in range(33):
   network = ip_network(f'{ip}/{mask}', 0)
   if network.network_address == net:
       print(32 - mask)

