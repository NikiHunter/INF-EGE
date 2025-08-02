//Автор: И.Свистун
### 
uses School;  
var s: HashSet<string>:=['0', '128', '192', '224', '240', '248', '252', '254'];
var set1:='229.117.112.0'; var m:=300;
foreach var z in s do
 begin    
  var x:= new CalcIP('229.117.114.172', '255.255.'+z+'.0');
  var n:=x.GenAddr.sel(t -> t.ToS).Sel(t -> t[ :t.IndexOf(',')+1]).toA;  
  if (n.Cnt>0) and (n[0]=set1) then m:=min(m, 16+bin(z.tointeger).Cnt('1')) ; 
  end;   println(m)
