# Автор: М. Ишимов

from ipaddress import *
ip = ip_address('134.73.209.97')
net = ip_address('134.73.192.0')
for mask in range(33):
   network = ip_network(f'{ip}/{mask}', 0)
   if net == network.network_address:
       mask = network.netmask
       byte3 = str(mask).split('.')[2]
       print(byte3)
       break


