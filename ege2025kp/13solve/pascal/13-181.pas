//Автор: И.Свистун
### 
uses School;  
var y:= new CalcIP('250.135.101.80', '255.255.255.248');
y.GenAddrBin.sel(t -> t.ToS).wh(t -> t.Cnt('0').Divs(3)).cnt.pr; 

  