from ipaddress import *
for i in range(31,-1,-1): 
    net1 = ip_network("118.222.130.140/"+ str(i),0)
    net2 = ip_network("118.222.201.140/"+ str(i),0)
    sub1 = str(net1).split("/")
    sub2 = str(net2).split("/")
    if sub1[0] == sub2[0]:# одна сеть
        print(net1.netmask)
        break
        
    

    
