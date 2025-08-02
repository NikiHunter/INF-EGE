//Автор: И.Свистун
### 
uses School;  
var s: HashSet<string>:=['0', '128', '192', '224', '240', '248', '252', '254', '255'];
var set1:='190.120.251.0'; var m:=0;
foreach var z in s do
 begin    
  var x:= new CalcIP('190.120.251.78', '255.255.'+z+'.0');
  var n:=x.GenAddr.sel(t -> t.ToS).Sel(t -> t[ :t.IndexOf(',')+1]).toA;  
  if (n.Cnt>0) and (n[0]=set1) then m:=max(m, 16-bin(z.tointeger).Cnt('1')); 
  end;   print(m)
//наибольшее количество нулей=32-наименьшее кол-во 1 (32-16-кол-во 1 в 3 октете)