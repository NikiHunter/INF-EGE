//Автор И. Свистун
###
uses school;
function net(n: integer): string:='0'*(8-bin(n).Count)+bin(n);
function addr(w,x,y,z: integer): string:=net(w)+'.'+net(x)+'.'+net(y)+'.'+net(z);
var s: HashSet<integer>:=[0, 128, 192, 224, 240, 248, 252, 254, 255];
var k:=300;
      foreach var y in s do
      if (y and 175)<>(y and 160) then
       if not(addr(255,255,y,0).Contains('0.1')) then  k:=min(y,k);
         print(k)
