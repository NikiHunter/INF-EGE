﻿//Автор И. Свистун
###
uses school;
var s: HashSet<string>:=['0', '128', '192', '224', '240', '248', '252', '254', '255'];
var set1:='111.3.160.0'; var m:=0;
foreach var z in s do
 begin    
  var x:= new CalcIP('111.3.161.27', '255.255.'+z+'.0');
  var n:=x.GenAddr.sel(t -> t.ToS).Sel(t -> t[ :t.IndexOf(',')+1]).toA;  
  if (n.cnt >= 2000)and (n[0]=set1) then m+=1;
  end;   
  println(m)

