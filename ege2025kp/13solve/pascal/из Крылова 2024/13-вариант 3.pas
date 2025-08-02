//Автор: И.Свистун
### 
uses School;  
var y:= new CalcIP('23.140.159.160', '255.255.252.0');
y.GenAddrBin.sel(t -> t.ToS).wh(t -> t[^16:].Cnt('1') <= t[:17].Cnt('1')).cnt.pr; 

  