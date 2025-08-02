//Автор: И.Свистун
### 
uses School;  
var s: HashSet<string>:=['0', '128', '192', '224', '240', '248', '252', '254'];
var set1:='193.22.209.128'; var m:=300;
foreach var z in s do
 begin    
  var x:= new CalcIP('193.22.209.132', '255.255.255.'+z);
  var n:=x.GenAddr.sel(t -> t.ToS).Sel(t -> t[ :t.IndexOf(',')+1]).toA;  
  if (n.Cnt>0) and (n[0]=set1) then m:=min(m, 8-bin(z.tointeger).Cnt('1')); 
  end;   print(m)
//наименьшее количество нулей = 32-наибольшее кол-во единиц (24+кол-во 1 в 4 октете)