//Автор И. Свистун
###
uses school;
var q: HashSet<string>:=['0', '128', '192', '224', '240', '248', '252', '254'];
var ip1:='45.214.123.173'; var mm:=0;
foreach var z in q do
 begin    
  var x:= new CalcIP('45.214.123.131', '255.255.255.'+z);
  var n:=x.GenAddr.sel(t -> t.ToS).Sel(t -> t[ :t.IndexOf(',')+1]).toA;    
  if (n.Cnt>0) and not(ip1 in n) and (n[n.H]>'45.214.123.131')
  then mm:=max(24+ bin(z.tointeger).Cnt('1'),mm); 
  end;  
  print(mm)
//необходима проверка, чтобы IP-адреса не совпадали с широковещательными и 
//самим адресом сети


