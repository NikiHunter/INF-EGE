from ipaddress import ip_network

for mask in range(1, 33):
    net = ip_network(f'149.238.225.115/{mask}', strict=False)
    print(net.network_address, net.netmask)
