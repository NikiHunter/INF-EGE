//Автор: И.Свистун
###
uses school; 
 var y:= new CalcIP('217.19.128.131', '255.255.192.0');
var s:=y.GenAddr.sel(t -> t.ToS).Sel(t -> t[ :t.IndexOf(',')+1]).toA;  
println(s[0]) ;


