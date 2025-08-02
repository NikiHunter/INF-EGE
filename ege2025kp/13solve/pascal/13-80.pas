//Автор: И.Свистун
###
uses school;
function net(n: integer): string:='0'*(8-bin(n).Count)+bin(n);
function addr(w,x,y,z: integer): string:=net(w)+'.'+net(x)+'.'+net(y)+'.'+net(z);
var s: HashSet<integer>:=[0, 128, 192, 224, 240, 248, 252, 254, 255];
var k:=300;
    foreach var y in s do
      foreach var z in s do
      if ((y and 208)=192) and (z and 27=0) and
      not(addr(255,255,y,z).Contains('0.1')) then k:=min(k,y);
      println(k);
      
//другое решение 
var q: HashSet<string>:=['0', '128', '192', '224', '240', '248', '252', '254'];
var set1:='111.81.192.0'; var mm:=300;
foreach var z in q do
 begin    
  var x:= new CalcIP('111.81.208.27', '255.255.'+z+'.0');
  var n:=x.GenAddr.sel(t -> t.ToS).Sel(t -> t[ :t.IndexOf(',')+1]).toA;  
  if (n.Cnt>0) and (set1=n[0]) then  mm:= min(mm,z.tointeger); 
  end; print(mm);     