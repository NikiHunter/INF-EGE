from ipaddress import ip_network, ip_address

ip1 = "161.137.200.35"
ip2 = ip_address("161.137.150.118")
bAll = [0, 128, 192, 224, 240, 248, 252, 254, 255]
for b in bAll[::-1]:
  net = ip_network(f"{ip1}/255.255.{b}.0", 0)
  if ip2 in net:
    print( b )
    break