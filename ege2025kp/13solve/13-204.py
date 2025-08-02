from ipaddress import ip_network, ip_address

ip1 = "193.45.192.104"
ip2 = ip_address("193.45.206.210")
bAll = [0, 128, 192, 224, 240, 248, 252, 254, 255]
for b in bAll[::-1]:
  net = ip_network(f"{ip1}/255.255.{b}.0", 0)
  if ip2 in net:
    print( b )
    break