from ipaddress import ip_network
count = 0
for ip in ip_network('94.253.128.0/255.255.128.0'):
  b = f'{ip:b}'
  if b.count('1') % 6 != 0 and b.endswith('101'):
    count += 1
print( count )