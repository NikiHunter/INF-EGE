# Автор: М. Ишимов

from ipaddress import *
mask = ip_address('255.255.255.224')
for A in range(256):
   ip = ip_address(f'227.31.{A}.139')
   network = ip_network(f'{ip}/{mask}', 0)
   if ip not in [network.network_address, network.broadcast_address]:
       if all( f'{ip:b}'[:16].count('0') <= f'{ip:b}'[16:].count('0')
           for ip in network):
           print(A)
