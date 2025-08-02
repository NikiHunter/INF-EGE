//Автор: И.Свистун
###
uses school; 
function net(n: integer): string:='0'*(8-bin(n).Count)+bin(n);
function addr(w,x,y,z: integer): string:=net(w)+'.'+net(x)+'.'+net(y)+'.'+net(z);
println (addr(255,255,224,0));
println(addr(206,158,124,67));
println(dec(net(124)[4:]+net(67),2)); 

//другое решение
var y:= new CalcIP('206.158.124.67', '255.255.224.0');
var k:= y.GenAddr.sel(t -> t.ToS)
.Sel(t -> t[ :t.IndexOf(',')+1])
.Numerate
.wh(\(n,t) -> t='206.158.124.67').toA;
print(k[0][0]-1);
//номер берем в ответ на 1 меньше, т.к. на 1 номере стоит адрес сети
// из-за этого номера сдвигаются
