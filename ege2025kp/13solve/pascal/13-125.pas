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
     if (64 and y = 64) and (z and 13 =0) and
     not(addr(255,x,y,z).Contains('0.1')) then k+=1; 
println(k);

//другое решение 
var q: HashSet<string>:=['0', '128', '192', '224', '240', '248', '252', '254'];
var set1:='131.149.64.0'; var mm:=0;
foreach var y in q do
 begin    
  var x1:= new CalcIP('131.149.64.13', '255.255.'+y+'.0');
  var n1:=x1.GenAddr.sel(t -> t.ToS).Sel(t -> t[ :t.IndexOf(',')+1]).toA;  
  if (n1.Cnt>0) and (set1=n1[0]) then mm+=1;  
  var x2:= new CalcIP('131.149.64.13', '255.255.255.'+y);
  var n2:=x2.GenAddr.sel(t -> t.ToS).Sel(t -> t[ :t.IndexOf(',')+1]).toA;  
  if (n2.Cnt>0) and (set1=n2[0]) then mm+=1; 
  end; print(mm)  

