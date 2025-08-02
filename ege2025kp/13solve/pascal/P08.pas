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
      if (net(x and 222)=net(222))and ((y and 130)=(y and 201)) and (z and 140=0) then 
      begin println(addr(255,x,y,z)); k:=max(k,y); end;
      println(k);
      
//другое решение
var q: HashSet<string>:=['0', '128', '192', '224', '240', '248', '252', '254', '255'];
var set1:='118.222.130.140'; var m:=0; 
foreach var z in q do
 begin    
  var x:= new CalcIP('118.222.201.140', '255.255.'+z+'.0');
  var n:=x.GenAddr.sel(t -> t.ToS).Sel(t -> t[ :t.IndexOf(',')+1]).toA;  
  if (n.Cnt>0) and (set1 in n) then m:=max(m, z.ToInteger);  
  end;  println(m);