//Автор: И.Свистун
### 
uses School;  
var y:= new CalcIP('94.159.76.0', '255.255.255.128');
y.GenAddrBin.sel(t -> t.ToS).sel(t -> t.Cnt('0')).min.pr; 

  