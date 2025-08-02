from ipaddress import ip_network
count = 0
for ip in ip_network('112.160.0.0/255.240.0.0'):
  b = f'{ip:b}'
  if b.count('1') % 3 != 0:
    count += 1
print( count )