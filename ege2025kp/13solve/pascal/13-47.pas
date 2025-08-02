//Автор: И.Свистун
###
uses school; 
 var y:= new CalcIP('224.24.254.134', '255.255.224.0');
var s:=y.GenAddr.sel(t -> t.ToS).Sel(t -> t[ :t.IndexOf(',')+1]).toA;  
println(s[0]) ;


