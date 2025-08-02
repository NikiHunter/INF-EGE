//Автор: И.Свистун
### 
uses School;  
var y:= new CalcIP('154.233.0.0', '255.255.0.0');
y.GenAddrBin.sel(t -> t.ToS).wh(t -> t[^1]='0').cnt.pr; 

  