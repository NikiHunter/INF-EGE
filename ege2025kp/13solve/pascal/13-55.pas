//Автор: И.Свистун
###
uses school;
function net(n: integer): string:='0'*(8-bin(n).Count)+bin(n);
function addr(w,x,y,z: integer): string:=net(w)+'.'+net(x)+'.'+net(y)+'.'+net(z);
var s: HashSet<integer>:=[0, 128, 192, 224, 240, 248, 252, 254, 255];
  foreach var x in s do 
    foreach var y in s do
      foreach var z in s do
      if (net(x and 228)=net(228))and ((y and 60)=56) and (z and 240=0)
      and not(addr(255,x,y,z).Contains('0.1'))then println(y); 
     