from ipaddress import ip_network
count = 0
for ip in ip_network('172.16.168.0/255.255.248.0'):
  b = f'{ip:b}'
  if b.count('1') % 5 != 0:
    count += 1
print( count )