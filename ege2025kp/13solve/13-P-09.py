from ipaddress import *
k = 0
for i in range(32):  
    net = ip_network("71.192.0.12/"+ str(i),0)
    sub = str(net).split("/")
    if sub[0] == '71.192.0.0':# если нужная сеть
        k+=1
print(k)

        
    

    
