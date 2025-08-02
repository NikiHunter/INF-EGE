//Автор: И.Свистун
### 
uses School;  
var y:= new CalcIP('213.0.0.0', '255.192.0.0');
y.GenAddrBin.sel(t -> t.ToS).wh(t -> t.Contains('111')).cnt.pr; 

  