//Автор: И.Свистун
###
uses school; 
var x:= New CalcIp('217.16.246.2', '255.255.252.0');
var n:=x.GenAddr.sel(t -> t.ToS).Sel(t -> t[ :t.IndexOf(',')+1]).toA;  
println(n[0]); 

