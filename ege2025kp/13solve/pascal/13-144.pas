//Автор И. Свистун
###
uses school;
var q: HashSet<string>:=['0', '128', '192', '224', '240', '248', '252', '254', '255'];
var ip1:='118.187.65.115'; var mm:=0;
foreach var z in q do
 begin    
  var x:= new CalcIP('118.187.59.255', '255.255.'+z+'.0');
  var n:=x.GenAddr.sel(t -> t.ToS).Sel(t -> t[ :t.IndexOf(',')+1]).toA;    
  if (n.Cnt>0) and not(ip1 in n) and (n[n.H]>'118.187.59.255')
  then mm:=max(16+ bin(z.tointeger).Cnt('1'),mm); 
  end;  
  print(mm)