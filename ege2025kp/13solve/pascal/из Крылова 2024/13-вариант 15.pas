//Автор: И.Свистун
###
uses school;
var q: HashSet<string>:=['0', '128', '192', '224', '240', '248', '252', '254', '255'];
var set1:='44.44.224.0'; var mm:=0;
foreach var z in q do
 begin    
  var x:= new CalcIP('44.44.229.28', '255.255.'+z+'.0');
  var n:=x.GenAddr.sel(t -> t.ToS).Sel(t -> t[ :t.IndexOf(',')+1]).toA;  
  if (n.Cnt>0) and (set1=n[0]) then 
    mm:=max((bin(255)+bin(255)+bin(z.tointeger)).cnt('1'),mm);  
  end; print(mm)  