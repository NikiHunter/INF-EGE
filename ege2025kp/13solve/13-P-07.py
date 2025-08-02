from ipaddress import *
for i in range(32): 
    net = ip_network("124.128.112.142/"+ str(i),0)
    sub = str(net).split("/") # выделяем только IP
    if sub[0] == "124.128.64.0":# нужная сеть
        print(net.netmask)


        
    

    
