//Автор: И.Свистун
### 
uses School;  
var s: HashSet<integer>:=[0, 128, 192, 224, 240, 248, 252, 254, 255];
var m:=300;
     foreach var z in s do
       begin    
  var y:= new CalcIP('134.97.250.117', '255.255.'+z.ToS+'.0');
  var b:=y.GenAddrBin.sel(t -> t.ToS).wh(t -> t[^16:].Cnt('0') <= t[:17].Cnt('0')).cnt; 
  if (y.GenAddrBin.cnt=b) then  m:=min(m,z);
  end;
  print(m);
  