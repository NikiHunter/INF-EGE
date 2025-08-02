//Автор И. Свистун
###
uses school;
function net(n: integer): string:='0'*(8-bin(n).Count)+bin(n);
function addr(w,x,y,z: integer): string:=net(w)+'.'+net(x)+'.'+net(y)+'.'+net(z);
var s: HashSet<integer>:=[0, 128, 192, 224, 240, 248, 252, 254, 255];
var k:=300;
 foreach var y in s do
 if ((y and 104)<>(y and 107)) and not addr(255,255,y,0).Contains('0.1') then k:=min(y,k); 
println(k);

// другое решение
var q: HashSet<string>:=['0', '128', '192', '224', '240', '248', '252', '254'];
var ip1:='117.137.107.95'; var mm:=300;
foreach var z in q do
 begin    
  var x:= new CalcIP('117.137.104.11', '255.255.'+z+'.0');
  var n:=x.GenAddr.sel(t -> t.ToS).Sel(t -> t[ :t.IndexOf(',')+1]).toA;  
  if (n.Cnt>0) and not(ip1 in n) 
  then mm:=min(z.tointeger,mm); 
  end;  print(mm)
