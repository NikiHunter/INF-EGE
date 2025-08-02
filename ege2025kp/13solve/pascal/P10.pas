//Автор: И.Свистун
###
uses school; 
var s: HashSet<integer>:=[0, 128, 192, 224, 240, 248, 252, 254];
var m:=300;
foreach var i in s do begin
var calc:= new CalcIP('195.157.132.140', '255.255.255.'+i.tostring);
if (calc.GenAddr.Count>39)then m:=min(m, calc.GenAddr.Count+2); end;
println(m);

//другое решение 
var q: HashSet<string>:=['0', '128', '192', '224', '240', '248', '252', '254'];
var mm:=3000000;
foreach var y in q do
 begin    
  var x:= new CalcIP('195.157.132.140', '255.255.255.'+y);
  var n:=x.GenAddr.sel(t -> t.ToS).Sel(t -> t[ :t.IndexOf(',')+1]).toA;  
  if (n.Cnt>0) and ('195.157.132.176' in n) then mm:=min(mm, n.cnt+2);  
   end; print(mm)  
