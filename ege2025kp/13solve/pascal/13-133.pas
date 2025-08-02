//Автор И. Свистун
###
uses school; 
var q: HashSet<string>:=['0', '128', '192', '224', '240', '248', '252', '254'];
var mm:=300000;
foreach var z in q do
 begin    
  var x:= new CalcIP('121.171.5.107', '255.255.255.'+z);
  var n:=x.GenAddr.sel(t -> t.ToS).Sel(t -> t[ :t.IndexOf(',')+1]).toA;    
  if (n.Cnt>0) and ('121.171.5.70' in n)then mm:=min(n.cnt,mm); 
  end;  
  print(mm+2)
  //на выходе добавляем адрес сети и широковещательный