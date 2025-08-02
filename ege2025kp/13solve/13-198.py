# Автор: М. Ишимов

from ipaddress import *
from fnmatch import *
ip = ip_address('243.46.4.198')
for mask in range(33):
   network = ip_network(f'{ip}/{mask}', 0)
   if fnmatch(str(network.netmask), '255.255.*.0'):
       if ip not in [network.network_address, network.broadcast_address]:
           if all(f'{ip:b}'[:16].count('0') <= f'{ip:b}'[16:].count('0')
               for ip in network):
               print(str(network.netmask).split('.')[2])
