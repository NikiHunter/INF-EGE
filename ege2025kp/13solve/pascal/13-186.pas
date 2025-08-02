//Автор: И.Свистун
### 
uses School;  
var y:= new CalcIP('99.65.32.0', '255.255.224.0');
y.GenAddrBin.sel(t -> t.ToS).wh(t -> t.Cnt('1')=t.Cnt('0')).cnt.pr; 

  