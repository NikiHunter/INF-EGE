//Автор И. Свистун
###
uses school; 
function net(n: integer): string:='0'*(8-bin(n).Count)+bin(n);
function addr(w,x,y,z: integer): string:=net(w)+'.'+net(x)+'.'+net(y)+'.'+net(z);
var s: HashSet<integer>:=[0, 128, 192, 224, 240, 248, 252, 254];
var k:=300; 
foreach var y in s do
  foreach var z in s do
if (175 and y <> 170 and y) and not(addr(255,255,y,z).Contains('0.1')) then 
    k:=min(addr(255,255,y,z).Cnt('1'), k); 
println(k); 

//другое решение ###uses school;
var q: HashSet<string>:=['0', '128', '192', '224', '240', '248', '252', '254','255'];
var ip1:='132.46.175.26'; var mm:=300;
foreach var z in q do
 begin    
  var x:= new CalcIP('132.46.170.130', '255.255.'+z+'.0');
  var n:=x.GenAddr.sel(t -> t.ToS).Sel(t -> t[ :t.IndexOf(',')+1]).toA;    
  if (n.Cnt>0) and not(ip1 in n) and (n[n.H]>'132.46.170.130')
  then mm:=min(16+ bin(z.tointeger).Cnt('1'),mm); 
  end;  
  print(mm)


