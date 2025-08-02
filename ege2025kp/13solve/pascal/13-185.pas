//Автор: И.Свистун
### 
uses School;  
var y:= new CalcIP('99.165.134.0', '255.255.254.0');
y.GenAddrBin.sel(t -> t.ToS).wh(t -> t.Cnt('1').Divs(3)).cnt.pr; 

  