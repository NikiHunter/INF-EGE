# Автор В.Н. Шубинкин

from ipaddress import ip_network

count = 0
for mask in range(1, 32):
    try:
        net = ip_network(f'115.53.128.0/{mask}')
        count += len(list(net.hosts())) >= 1000
    except:
        pass
print(count)
