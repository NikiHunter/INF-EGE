//Автор: И.Свистун
### 
uses School;  
var y:= new CalcIP('98.116.0.0', '255.252.0.0');
y.GenAddrBin.sel(t -> t.ToS).wh(t -> t.Cnt('0').Divs(2)).cnt.pr; 

  