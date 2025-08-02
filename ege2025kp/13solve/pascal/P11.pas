###
uses school; 
var s: HashSet<integer>:=[0, 128, 192, 224, 240, 248, 252, 254];
foreach var i in s do
if (35 and i <> 117 and i) then 
  begin println('*****',i, bin(i)); 
  var x:= New CalcIp('192.168.106.35', '255.255.255.'+i.tostring);
print(x); end;

