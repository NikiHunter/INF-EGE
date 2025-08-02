//Автор: И.Свистун
###
uses school; 
function net(n: integer): string:='0'*(8-bin(n).Count)+bin(n);
function addr(w,x,y,z: integer): string:=net(w)+'.'+net(x)+'.'+net(y)+'.'+net(z);
var n:=35-addr(255,255,255,224).IndexOf('0')-1; 
println(dec(net(157)[n:],2)); 

//другое решение
var y:= new CalcIP('162.198.0.157', '255.255.255.224');
var k:= y.GenAddr.sel(t -> t.ToS).Sel(t -> t[ :t.IndexOf(',')+1]).Numerate
.wh(\(n,t) -> t='162.198.0.157').print;
//номер берем в ответ на 1 меньше, т.к. на 1 номере стоит адрес сети
// из-за этого номера сдвигаются
