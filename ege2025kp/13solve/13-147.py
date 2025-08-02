# Автор В.Н. Шубинкин

from ipaddress import ip_network

for mask in range(16, 32):
    try:
        net1 = ip_network(f'191.131.175.201/{mask}', False)
        net2 = ip_network(f'191.131.160.170/{mask}', False)
        if net1 != net2:
            print(str(net1.netmask).split('.')[2])
            break
    except:
        pass
