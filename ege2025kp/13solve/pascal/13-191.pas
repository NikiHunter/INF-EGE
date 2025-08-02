//Автор: И.Свистун
### 
uses School;  
var s: HashSet<string>:=['0', '128', '192', '224', '240', '248', '252', '254'];
var set1:='111.7.92.32'; var m:=300;
foreach var z in s do
 begin    
  var x:= new CalcIP('111.7.92.52', '255.255.255.'+z);
  var n:=x.GenAddr.sel(t -> t.ToS).Sel(t -> t[ :t.IndexOf(',')+1]).toA;  
  if (n.Cnt>0) and (n[0]=set1) then m:=min(m, z.ToInteger);  
  end;   println(m);
