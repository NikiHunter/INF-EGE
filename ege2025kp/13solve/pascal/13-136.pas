//Автор И. Свистун
###
uses school; 
function net(n: integer): string:='0'*(8-bin(n).Count)+bin(n);
function addr(w,x,y,z: integer): string:=net(w)+'.'+net(x)+'.'+net(y)+'.'+net(z);
var s: HashSet<integer>:=[0, 128, 192, 224, 240, 248, 252, 254];
var k:=300; 
foreach var i in s do
if (76 and i <> 55 and i) then k:=min(addr(255,255,255,i).Cnt('1'), k);
println(k); 


