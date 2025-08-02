from ipaddress import ip_network
count = 0
for ip in ip_network('172.16.128.0/255.255.192.0'):
  b = f'{ip:b}'
  if b.count('1') % 2 != 0:
    count += 1
print( count )