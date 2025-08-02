# Автор В.Н. Шубинкин

from ipaddress import ip_network

for mask in range(16, 32):
    try:
        net1 = ip_network(f'132.46.175.26/{mask}', False)
        net2 = ip_network(f'132.46.170.130/{mask}', False)
        if net1 != net2:
            print(mask)
            break
    except:
        pass
