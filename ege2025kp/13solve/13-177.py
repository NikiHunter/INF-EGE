# Автор: М. Ишимов

from ipaddress import *
ip = ip_address('90.155.69.100')
net = ip_address('90.155.69.0')
ans = 0
for mask in range(33):
   network = ip_network(f'{ip}/{mask}', 0)
   if net == network.network_address:
       ans += 1
print(ans)



