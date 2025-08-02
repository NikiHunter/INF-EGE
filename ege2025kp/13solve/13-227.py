from ipaddress import ip_network
count = 0
for ip in ip_network('79.128.96.0/255.255.224.0'):
  b = f'{ip:b}'
  if b.count('1') % 7 != 0 and b.endswith('100'):
    count += 1
print( count )