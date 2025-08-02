//Автор: И.Свистун
### 
uses School;  
var y:= new CalcIP('116.29.170.89', '255.255.255.224');
y.GenAddrBin.sel(t -> t.ToS).wh(t -> t[^16:].Cnt('1') <= t[:17].Cnt('1')).cnt.pr; 

  