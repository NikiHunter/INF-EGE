# Автор: М. Ишимов

from ipaddress import *
ip = ip_address('229.117.114.172')
net = ip_address('229.117.112.0')
for mask in range(33):
   network = ip_network(f'{ip}/{mask}', 0)
   if network.network_address == net:
       print(mask)
       break
