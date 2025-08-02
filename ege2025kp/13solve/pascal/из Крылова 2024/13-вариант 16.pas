//Автор: И.Свистун
###
uses school;
var q: HashSet<integer>:=[128, 192, 224, 240, 248, 252, 254, 255];
var k:=0;
foreach var z in q do
if (z and 244 = 244) then k:=max(k, 32-bin(z).cnt('1'));
print(k)
