from ipaddress import ip_network, IPv4Address


for i in range(16, 33):
    ip = ip_network(f"152.217.69.70/{i}", False)
    ip1 = ip_network(f"152.217.125.80/{i}", False)
    print(69 & 1)
    print(125)
    
"""
from ipaddress import ip_network 192

for mask in range(30, 0, -1):
    try:
        net1 = ip_network(f'111.81.200.27/{mask}', False)
        net2 = ip_network(f'111.81.192.0/{mask}', False)
        if net1 == net2:
            print(len(list(net1)))
            break
    except:
        pass
"""
