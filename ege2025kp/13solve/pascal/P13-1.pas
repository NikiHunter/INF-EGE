//Автор: И.Свистун
###
uses school;
function net(n: integer): string:='0'*(8-bin(n).Count)+bin(n);
function addr(w,x,y,z: integer): string:=net(w)+'.'+net(x)+'.'+net(y)+'.'+net(z);
 
var q: HashSet<integer>:=[0, 128, 192, 224, 240, 248, 252, 254, 255];
  foreach var x in q do 
    foreach var y in q do
      foreach var z in q do
      if (net(x and 51)=net(51))and ((y and 208)= 192) and (z and 15=0) and 
      not addr(255,x,y,z).Contains('0.1') then 
        println(addr(255,x,y,z),addr(255,x,y,z).Cnt('1'));

     