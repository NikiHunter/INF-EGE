//Автор: И.Свистун
###
uses school;
var q: HashSet<string>:=['0', '128', '192', '224', '240', '248', '252', '254', '255'];
var m:=0;
foreach var z in q do
 begin    
  var x:= new CalcIP('121.171.15.70', '255.255.'+z+'.0');
  var n:=x.GenAddr.sel(t -> t.ToS).Sel(t -> t[ :t.IndexOf(',')+1]).toA;  
  if (n.Cnt>0) and ('121.171.3.68' in n) then m:=max(m, z.ToInteger);  
  end;  println(m);