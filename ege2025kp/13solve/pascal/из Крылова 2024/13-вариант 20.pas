//Автор: И.Свистун
###
uses school;
var q: HashSet<string>:=['0', '128', '192', '224', '240', '248', '252', '254'];
var set1:='99.188.115.192'; var mm:=0;
foreach var z in q do
 begin    
  var x:= new CalcIP('99.188.115.211', '255.255.255.'+z);
  var n:=x.GenAddr.sel(t -> t.ToS).Sel(t -> t[ :t.IndexOf(',')+1]).toA;  
  if (n.Cnt>0) and (set1=n[0]) then 
    mm:=max((bin(255)+bin(255)+bin(255)+bin(z.tointeger)).cnt('1'),mm);  
  end; print(mm)    