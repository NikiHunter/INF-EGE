//Автор: И.Свистун
### 
uses School;  
var s: HashSet<string>:=['0', '128', '192', '224', '240', '248', '252', '254'];
var set1:='90.155.69.0'; var k:=0;
foreach var z in s do
 begin    
  var x:= new CalcIP('90.155.69.100', '255.255.255.'+z);
  var n:=x.GenAddr.sel(t -> t.ToS).Sel(t -> t[ :t.IndexOf(',')+1]).toA;  
  if (n.Cnt>0) and (n[0]=set1) then k+=1;  
  end;   
println(k);