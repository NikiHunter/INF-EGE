//Автор: И.Свистун
###
uses school; 
var y:= new CalcIP('217.8.244.3', '255.255.252.0');
var n:=y.GenAddr.sel(t -> t.ToS).Sel(t -> t[ :t.IndexOf(',')+1]).toA;  
println(n[0]);

//другое решение ###uses school; 
var x:= New CalcIp('217.8.244.3', '255.255.252.0');
print(x); 
// и смотрим глазками строчку "IP адрес сети (Network)"
