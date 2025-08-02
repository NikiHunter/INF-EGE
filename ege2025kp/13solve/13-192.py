# Автор: М. Ишимов

from ipaddress import *
res = []
ip = ip_address('92.52.42.52')
net = ip_address('92.52.42.0')
for mask in range(33):
   network = ip_network(f'{ip}/{mask}', 0)
   if net == network.network_address:
       mask = network.netmask
       byte4 = str(mask).split('.')[3]
       res += [int(byte4)]
print(max(res))
