//Автор И. Свистун
###
uses school;
function net(n: integer): string:='0'*(8-bin(n).Count)+bin(n);
function addr(w,x,y,z: integer): string:=net(w)+'.'+net(x)+'.'+net(y)+'.'+net(z);
var s: HashSet<integer>:=[0, 128, 192, 224, 240, 248, 252, 254, 255];
var k:=300;
    foreach var y in s do
      foreach var z in s do
      if ((y and 75)=75) and (z and 91=64) and not(addr(255,255,y,z).Contains('0.1')) then 
      k:=min(addr(255,255,y,z).Cnt('0'), k); 
        print(2**k);
        
// другое решение
var q: HashSet<string>:=['0', '128', '192', '224', '240', '248', '252', '254'];
var m:=300000;
foreach var z in q do
 begin    
  var x:= new CalcIP('108.133.75.91', '255.255.255.'+z);
  var n:=x.GenAddr.sel(t -> t.ToS).Sel(t -> t[ :t.IndexOf(',')+1]).toA;  
  if (n.Cnt>0) and (n[0]='108.133.75.64') then m:=min(m, x.GenAddr.cnt);  
  end;  
  print(m+2)                  