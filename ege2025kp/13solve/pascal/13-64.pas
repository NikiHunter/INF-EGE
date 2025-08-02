﻿//Автор: И.Свистун
###
uses school;
function net(n: integer): string:='0'*(8-bin(n).Count)+bin(n);
function addr(w,x,y,z: integer): string:=net(w)+'.'+net(x)+'.'+net(y)+'.'+net(z);
var s: HashSet<integer>:=[0, 128, 192, 224, 240, 248, 252, 254, 255];
  foreach var x in s do 
    foreach var y in s do
      foreach var z in s do
      if (net(x and 32)=net(32))and ((y and 112)=64) and (z and 131=0) 
      and not(addr(255,x,y,z).Contains('0.1'))then println(y); 

//другое решение 
var q: HashSet<string>:=['0', '128', '192', '224', '240', '248', '252', '254'];
var set1:='214.32.64.0'; 
foreach var z in q do
 begin    
  var x:= new CalcIP('214.32.112.131', '255.255.'+z+'.0');
  var n:=x.GenAddr.sel(t -> t.ToS).Sel(t -> t[ :t.IndexOf(',')+1]).toA;  
  if (n.Cnt>0) and (n[0]=set1) then println(z);  
  end;      