from ipaddress import ip_network, ip_address

ip1 = "161.137.200.35"
ip2 = ip_address("161.137.150.118")
for ones in range(31,1,-1):
  net = ip_network(f"{ip1}/{ones}", 0)
  if ip2 in net:
    print( 2**(32-ones-1) )
    break