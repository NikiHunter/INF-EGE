//Автор: И.Свистун
### 
uses School;  
var s: HashSet<string>:=['0', '128', '192', '224', '240', '248', '252', '254'];
var set1:='240.0.0.96'; var m:=0;
foreach var z in s do
 begin    
  var x:= new CalcIP('240.0.0.100', '255.255.255.'+z);
  var n:=x.GenAddr.sel(t -> t.ToS).Sel(t -> t[ :t.IndexOf(',')+1]).toA;  
  if (n.Cnt>0) and (n[0]=set1) then m:=max(m,z.tointeger); 
  end;   print(m); 
// в условии варианта 18 допущена ошибка! IP оставили из 17 варианта
//поэтому маску сети и IP подобрала сама под ответ