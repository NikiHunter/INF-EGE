from ipaddress import ip_network, ip_address

ip1 = "176.213.225.119"
ip2 = ip_address("176.213.195.58")
bAll = [0, 128, 192, 224, 240, 248, 252, 254, 255]
for b in bAll[::-1]:
  net = ip_network(f"{ip1}/255.255.{b}.0", 0)
  if ip2 in net:
    print( b )
    break