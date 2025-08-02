# Автор: М. Ишимов

from ipaddress import *
ip = ip_address('151.168.147.193')
net = ip_address('151.168.147.128')
for mask in range(33):
   network = ip_network(f'{ip}/{mask}', 0)
   if network.network_address == net:
       print(mask)
