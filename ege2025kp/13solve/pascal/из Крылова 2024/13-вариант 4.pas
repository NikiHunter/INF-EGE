//Автор: И.Свистун
### 
uses School;  
var y:= new CalcIP('253.112.169.12', '255.255.254.0');
y.GenAddrBin.sel(t -> t.ToS).wh(t -> t[^16:].Cnt('1') >= t[:17].Cnt('1')).cnt.pr; 

  