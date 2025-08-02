//Автор: И.Свистун
### 
uses School;  
  var y:= new CalcIP('192.168.32.160', '255.255.255.240');
  y.GenAddrBin.sel(t -> t.ToS).wh(t -> t.Cnt('0') >21).cnt.print; 

  