//Автор: И.Свистун
###
uses school;
function net(n: integer): string:='0'*(8-bin(n).Count)+bin(n);
function addr(w,x,y,z: integer): string:=net(w)+'.'+net(x)+'.'+net(y)+'.'+net(z);
var s: HashSet<integer>:=[0, 128, 192, 224, 240, 248, 252, 254, 255];
var k:=0;
  foreach var x in s do 
    foreach var y in s do
      foreach var z in s do
      if (net(x and 117)=net(117))and ((y and 107)=(y and 121)) and (z and 80=0) and
      not(addr(255,x,y,z).Contains('0.1')) then k:=max(k,y); 
      print(k);
      
// другое решение
var q: HashSet<string>:=['0', '128', '192', '224', '240', '248', '252', '254', '255'];
var m:=0;
foreach var z in q do
 begin    
  var x:= new CalcIP('112.117.121.80', '255.255.'+z+'.0');
  var n:=x.GenAddr.sel(t -> t.ToS).Sel(t -> t[ :t.IndexOf(',')+1]).toA;  
  if (n.Cnt>0) and ('112.117.107.70' in n) then m:=max(m, z.ToInteger);  
  end;  println(m);