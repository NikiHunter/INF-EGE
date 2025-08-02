# С помощью prefixlen

from ipaddress import *
for i in range(32): 
    net = ip_network("15.51.208.15/"+ str(i),0)
    sub = str(net).split("/")
    if sub[0] == "15.51.192.0":# нужная сеть
        print(net.prefixlen)
        break 

# С помощью netmask
from ipaddress import *
for i in range(32):  
    net = ip_network("15.51.208.15/"+ str(i),0)
    sub = str(net).split("/")
    if sub[0] == "15.51.192.0":# нужная сеть
        x10 = int(net.netmask) # маска в 10СС
        x2 = bin(x10)[2:] # маска в 2СС
        print(x2.count('1'))
        break


       
    

    
