//Автор: И.Свистун
### 
uses School;  
var y:= new CalcIP('252.67.33.87', '255.252.0.0');
y.GenAddrBin.sel(t -> t.ToS).wh(t -> t[^16:].Cnt('1') > t[:17].Cnt('1')*2).cnt.pr; 

  