from ipaddress import ip_network, IPv4Address

address1 = '112.166.78.114'
address2 = '112.166.78.117'
for mask in range(30, 0, -1):
    try:
        net1 = ip_network(f'{address1}/{mask}', False)
        net2 = ip_network(f'{address2}/{mask}', False)
        if (net1 != net2
                and IPv4Address(address1) in net1.hosts()
                and IPv4Address(address2) in net2.hosts()):
            print(mask)
            break
    except:
        pass
