import ipaddress


ip_addr, ip_2 = ipaddress.IPv4Address("111.81.200.27"), ipaddress.IPv4Address("111.81.192.0")
for mask in range(1, 33):
    mask_ = ipaddress.IPv4Network(f"0.0.0.0/{mask}").netmask
    if int(ip_addr) & int(mask_) == int(ip_2):
        print(mask_)
