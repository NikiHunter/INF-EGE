# Автор В.Н. Шубинкин

from ipaddress import ip_network

for mask in range(16, 32):
    try:
        net1 = ip_network(f'193.175.175.231/{mask}', False)
        net2 = ip_network(f'193.175.176.118/{mask}', False)
        if net1 != net2:
            print(str(net1.netmask).split('.')[2])
            break
    except:
        pass
