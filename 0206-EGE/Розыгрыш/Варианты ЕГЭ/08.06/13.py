from ipaddress import ip_network


ip_addr = ip_network("119.83.208.27", strict=False).network_address
ip_to = ip_network("119.83.192.0", strict=False).network_address

for mask in range(1, 33):
    ip_mask = ip_network(f"0.0.0.0/{mask}", strict=False).netmask
    if (int(ip_addr) & int(ip_mask)) == int(ip_to):
        print(sum([bin(int(i))[2:].count("1") for i in str(ip_mask).split(".")]),
              [bin(int(i))[2:] for i in str(ip_mask).split(".")], mask)
