from ipaddress import *
Min = 2**32
for i in range(32):  
    net1 = ip_network("195.157.132.140/"+ str(i),0)
    net2 = ip_network("195.157.132.176/"+ str(i),0)
    sub1 = str(net1).split("/")
    sub2 = str(net2).split("/")
    if sub1[0] == sub2[0]:# одна сеть
        k = net1.num_addresses   # считаем кол-во IP
        if k < Min:
            Min = k
print(Min)
        
    

    
