//Автор И. Свистун
###
uses school;
var q: HashSet<string>:=['0', '128', '192', '224', '240', '248', '252', '254'];
var ip1:='143.175.79.156'; var mm:=0;
foreach var z in q do
 begin    
  var x:= new CalcIP('143.175.103.191', '255.255.255.'+z);
  var n:=x.GenAddr.sel(t -> t.ToS).Sel(t -> t[ :t.IndexOf(',')+1]).toA;    
  if (n.Cnt>0) and not(ip1 in n) and (n[n.H]>'143.175.103.191')
  then mm:=max(24+ bin(z.tointeger).Cnt('1'),mm); 
  end;  
  print(mm)


