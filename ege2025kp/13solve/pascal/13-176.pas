//Автор: И.Свистун
### 
uses School;  
var s: HashSet<string>:=['0', '128', '192', '224', '240', '248', '252', '254'];
var set1:='180.2.224.0'; var m:=0;
foreach var z in s do
 begin    
  var x:= new CalcIP('180.2.252.76', '255.255.'+z+'.0');
  var n:=x.GenAddr.sel(t -> t.ToS).Sel(t -> t[ :t.IndexOf(',')+1]).toA;  
  if (n.Cnt>0) and (n[0]=set1) then m:=max(m, z.ToInteger); 
  end;   println(m); 
