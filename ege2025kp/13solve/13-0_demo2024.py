def ip2bin( sIp ):
  a = [int(o) for o in sIp.split('.')]
  n = a[0]*256**3 + a[1]*256**2 + a[2]*256 + a[3]
  return f'{n:b}'

mask = ip2bin( '255.255.255.240' )
zeroBits = mask.count('0')

print( 2**zeroBits//2 )
