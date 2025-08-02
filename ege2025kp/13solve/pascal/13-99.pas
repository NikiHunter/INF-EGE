//Автор: И.Свистун
###
uses school;
function net(n: integer): string:='0'*(8-bin(n).Count)+bin(n);
function addr(w,x,y,z: integer): string:=net(w)+'.'+net(x)+'.'+net(y)+'.'+net(z);
var s: HashSet<integer>:=[0, 128, 192, 224, 240, 248, 252, 254, 255];
var m:=0;
    foreach var y in s do
      foreach var z in s do
      if ((y and 70)=64) and (z and 47=0) and
      not(addr(255,255,y,z).Contains('0.1')) then 
        m:=max(m, addr(255,255,y,z).Cnt('1'));  print(m);
