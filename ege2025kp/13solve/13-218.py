from ipaddress import ip_network, ip_address

ip1 = "154.63.206.129"
ip2 = ip_address("154.63.100.75")
for ones in range(31,1,-1):
  net = ip_network(f"{ip1}/{ones}", 0)
  if ip2 in net:
    print( 2**(32-ones-1) )
    break