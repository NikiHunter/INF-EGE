//Автор: И.Свистун
###
uses school; 
 var y:= new CalcIP('217.13.163.133', '255.255.252.0');
var s:=y.GenAddr.sel(t -> t.ToS).Sel(t -> t[ :t.IndexOf(',')+1]).toA;  
println(s[0]) ;


