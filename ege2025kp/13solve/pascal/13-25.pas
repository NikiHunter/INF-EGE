//Автор: И.Свистун
###
uses school; 
var x:= New CalcIp('145.92.137.88', '255.255.240.0');
var n:=x.GenAddr.sel(t -> t.ToS).Sel(t -> t[ :t.IndexOf(',')+1]).toA;  
println(n[0]);

