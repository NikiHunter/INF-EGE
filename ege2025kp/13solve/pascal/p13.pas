//Автор: И.Свистун
###
uses school;
var m:=256; var mask:='255.255.'; var k:=16;
var s: HashSet<integer>:=[0, 128, 192, 224, 240, 248, 252, 254,255];
foreach var i in s do  
   if (208 and i=192) then m:=min(m,i);
println(mask+m.tostring+'.0', '***',k+bin(m).Cnt('1'));

// другое решение
var s1: HashSet<string>:=['0', '128', '192', '224', '240', '248', '252', '254'];
var set1:='15.51.192.0';var b:=300;
foreach var z in s1 do
 begin    
  var x:= new CalcIP('15.51.208.15', '255.255.'+z+'.0');
  var n:=x.GenAddr.sel(t -> t.ToS).Sel(t -> t[ :t.IndexOf(',')+1]).toA;  
  if (n.Cnt>0) and (n[0]=set1) then 
   b:=min((bin(255)+bin(255)+bin(z.tointeger)).cnt('1'),b);  
  end;   println(b);
