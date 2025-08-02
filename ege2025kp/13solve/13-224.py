from ipaddress import ip_network
count = 0
for ip in ip_network('115.198.0.0/255.254.0.0'):
  b = f'{ip:b}'
  if b.count('1') % 5 == 0:
    count += 1
print( count )