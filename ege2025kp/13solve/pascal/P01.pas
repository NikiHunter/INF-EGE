//Автор: И.Свистун
###
uses school;
function net(n: integer): string:='0'*(8-bin(n).Count)+bin(n);
function addr(w,x,y,z: integer): string:=net(w)+'.'+net(x)+'.'+net(y)+'.'+net(z);
var n:=35-addr(255,255,240,0).IndexOf('0')-9; 
println(dec(net(75)[n:]+net(44),2)); 

//другое решение 
var y:= new CalcIP('162.198.75.44', '255.255.240.0');
var k:= y.GenAddr.sel(t -> t.ToS).Sel(t -> t[ :t.IndexOf(',')+1]).Numerate
.wh(\(n,t) -> t='162.198.75.44').toA;
print(k[0][0]-1);
//номер берем в ответ на 1 меньше, т.к. на 1 номере стоит адрес сети
// из-за этого номера сдвигаются
