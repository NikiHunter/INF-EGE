//Автор: И.Свистун
###
uses school; 
var x:= New CalcIp('12.16.196.10', '255.255.224.0');
var n:=x.GenAddr.sel(t -> t.ToS).Sel(t -> t[ :t.IndexOf(',')+1]).toA;  
println(n[0]);

