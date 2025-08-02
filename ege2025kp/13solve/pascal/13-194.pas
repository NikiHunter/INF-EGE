//Автор: И.Свистун
### 
uses School;  
var x:= new CalcIP('186.135.80.0', '255.255.252.0');
x.GenAddrBin.sel(t -> t.ToS).wh(t -> t[^16:].Cnt('1') < t[:17].Cnt('1')).cnt.pr; 

// другой способ решения
var k:=0;
for var y:=80 to 83 do
  for var z:=0 to 255 do
     if (bin(186).Cnt('1')+bin(135).Cnt('1') > bin(y).Cnt('1')+bin(z).Cnt('1')) then k+=1; 
  print(k);
