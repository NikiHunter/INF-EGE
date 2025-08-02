from ipaddress import ip_network

ip_addr = ip_network("170.155.137.181").network_address
ip_net_go = ip_network("170.155.136.0").network_address

for mask in range(1, 33):
    net_mask = ip_network(f"0.0.0.0/{mask}").netmask
    if int(ip_addr) & int(net_mask) == int(ip_net_go):
        print(net_mask, mask)  # НИКОГДА НЕ ПИСАТЬ ТУТ break
