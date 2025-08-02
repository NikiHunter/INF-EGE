//Автор: И.Свистун
### 
uses School;  
function net(n: integer): string:='0'*(8-bin(n).Count)+bin(n);
var s: HashSet<string>:=['0', '128', '192', '224', '240', '248', '252', '254'];
var set1:='151.168.147.128'; var m:=0;
foreach var z in s do
 begin    
  var x:= new CalcIP('151.168.147.193', '255.255.255.'+z);
  var n:=x.GenAddr.sel(t -> t.ToS).Sel(t -> t[ :t.IndexOf(',')+1]).toA;  
  if (n.Cnt>0) and (n[0]=set1) then m:=max(m, 24+bin(z.tointeger).Cnt('1')) ; 
  end;   println(m)
