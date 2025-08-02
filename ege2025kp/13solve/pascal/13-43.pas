//Автор: И.Свистун
###
uses school; 
 var y:= new CalcIP('217.9.142.131', '255.255.192.0');
var s:=y.GenAddr.sel(t -> t.ToS).Sel(t -> t[ :t.IndexOf(',')+1]).toA;  
println(s[0]) ;

//другое решение
var x:= New CalcIp('217.9.142.131', '255.255.192.0');
print(x); 
// и смотрим строчку   //IP адрес сети (Network)              