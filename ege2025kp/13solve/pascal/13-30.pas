//Автор: И.Свистун
###
uses school; 
function net(n: integer): string:='0'*(8-bin(n).Count)+bin(n);
function addr(w,x,y,z: integer): string:=net(w)+'.'+net(x)+'.'+net(y)+'.'+net(z);
var n:=35-addr(255,255,255,224).IndexOf('0')-1; 
println(dec(net(227)[n:],2));


