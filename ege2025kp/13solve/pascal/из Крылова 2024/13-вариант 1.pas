//Автор: И.Свистун
### 
uses School;  
var y:= new CalcIP('142.108.56.118', '255.255.255.240');
y.GenAddrBin.sel(t -> t.ToS).wh(t -> t[^16:].Cnt('1') > t[:17].Cnt('1')).cnt.pr; 

  