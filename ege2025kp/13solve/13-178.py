# Автор: М. Ишимов

from ipaddress import *
ip = ip_address('120.216.74.153')
net = ip_address('120.216.0.0')
res = []
for mask in range(33):
   network = ip_network(f'{ip}/{mask}', 0)
   if net == network.network_address:
       res.append(network.num_addresses)
print(max(res))




