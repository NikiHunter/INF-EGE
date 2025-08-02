# Автор: М. Ишимов

from ipaddress import *
mask = ip_address('255.255.254.0')
for A in range(256):
   ip = ip_address(f'159.242.{A}.223')
   network = ip_network(f'{ip}/{mask}', 0)
   if ip not in [network.network_address, network.broadcast_address]:
       if all( f'{ip:b}'[:16].count('0') < f'{ip:b}'[16:].count('0')
           for ip in network):
           print(A)
