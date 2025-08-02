//Автор И. Свистун
###
uses school; 
function net(n: integer): string:='0'*(8-bin(n).Count)+bin(n);
function addr(w,x,y,z: integer): string:=net(w)+'.'+net(x)+'.'+net(y)+'.'+net(z);
var s: HashSet<integer>:=[0, 128, 192, 224, 240, 248, 252, 254];
var k:=300; 
foreach var i in s do
if (121 and i <> 156 and i) then k:=min(addr(255,255,255,i).Cnt('1'), k);
println(k); 

// другое решение ### uses school;
var q: HashSet<string>:=['0', '128', '192', '224', '240', '248', '252', '254'];
var set1:='151.172.115.121'; var mm:=300;
foreach var z in q do
 begin    
  var x:= new CalcIP('151.172.115.156', '255.255.255.'+z);
  var n:=x.GenAddr.sel(t -> t.ToS).Sel(t -> t[ :t.IndexOf(',')+1]).toA;  
  if (n.Cnt>0) and not(set1 in n) 
  then mm:=min(24+bin(z.tointeger).cnt('1'),mm); ;
  end;  print(mm)

