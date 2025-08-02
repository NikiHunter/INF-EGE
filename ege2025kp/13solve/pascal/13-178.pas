//Автор: И.Свистун
### 
uses School;  
var s: HashSet<string>:=['0', '128', '192', '224', '240', '248', '252', '254'];
var set1:='120.216.0.0'; var mm:=0;
foreach var z in s do    
  if (216 and z.ToInteger = 216) then 
    begin
    var y:= new CalcIP('120.216.74.153', '255.'+z+'.0.0');   
    var m:=y.GenAddr.sel(t -> t.ToS).Sel(t -> t[ :t.IndexOf(',')+1]).toA;  
    if (m.Cnt>0) and (m[0]=set1) then mm:=max(mm,y.GenAddr.cnt); end;
  print(mm)
