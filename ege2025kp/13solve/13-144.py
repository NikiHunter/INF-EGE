# Автор В.Н. Шубинкин

from ipaddress import ip_network, IPv4Address

address1 = '118.187.59.255'
address2 = '118.187.65.115'
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
