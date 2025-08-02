//Автор: И.Свистун
### 
uses School;  
var y:= new CalcIP('135.221.128.0', '255.255.128.0');
y.GenAddrBin.sel(t -> t.ToS).sel(t -> t.Cnt('1')).min.pr; 

  