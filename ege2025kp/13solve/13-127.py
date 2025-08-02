# Автор В.Н. Шубинкин

from ipaddress import ip_network

for mask in range(30, 0, -1):
    try:
        net1 = ip_network(f'111.81.200.27/{mask}', False)
        net2 = ip_network(f'111.81.192.0/{mask}', False)
        if net1 == net2:
            print(len(list(net1)))
            break
    except:
        pass
