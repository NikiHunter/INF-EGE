//Автор: И.Свистун
### 
uses School;  
var y:= new CalcIP('99.64.0.0', '255.192.0.0');
y.GenAddrBin.sel(t -> t.ToS).wh(t -> t[^2:]='11').cnt.pr; 

  