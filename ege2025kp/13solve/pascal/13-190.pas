//Автор: И.Свистун
### 
uses School;  
var y:= new CalcIP('124.8.0.0', '255.248.0.0');
y.GenAddrBin.sel(t -> t.ToS).sel(t -> t.Cnt('0')).max.pr; 

  