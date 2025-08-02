//Автор: И.Свистун
### 
uses School;  
var y:= new CalcIP('204.252.0.0', '255.255.0.0');
y.GenAddrBin.sel(t -> t.ToS).sel(t -> t.Cnt('1')).max.pr; 

  