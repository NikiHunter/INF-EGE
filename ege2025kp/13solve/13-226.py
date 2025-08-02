from ipaddress import ip_network
count = 0
for ip in ip_network('102.141.0.0/255.255.192.0'):
  b = f'{ip:b}'
  if b.count('1') % 7 == 0 and b.endswith('1011'):
    count += 1
print( count )