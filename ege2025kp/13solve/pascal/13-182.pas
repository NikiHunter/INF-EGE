//Автор: И.Свистун
### 
uses School;  
var y:= new CalcIP('143.198.224.0', '255.255.240.0');
y.GenAddrBin.sel(t -> t.ToS).wh(t -> t.Cnt('0').NotDivs(2)).cnt.pr; 

  