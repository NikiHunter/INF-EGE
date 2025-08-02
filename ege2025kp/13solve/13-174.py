# Автор: М. Ишимов

from ipaddress import *
ip = ip_address('193.22.209.132')
net = ip_address('193.22.209.128')
for mask in range(33):
   network = ip_network(f'{ip}/{mask}', 0)
   if network.network_address == net:
       print(32 - mask)

