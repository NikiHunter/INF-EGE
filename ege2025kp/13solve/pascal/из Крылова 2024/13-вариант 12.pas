//Автор: И.Свистун
### 
uses School;  
     foreach var a in (0..255) do
       begin    
  var y:= new CalcIP('64.129.'+a.ToS+'.10', '255.255.252.0');
  var b:=y.GenAddrBin.sel(t -> t.ToS).wh(t -> t[^16:].Cnt('1') >= t[:17].Cnt('1')).cnt;
  if (y.GenAddrBin.cnt=b) then begin print(a);break; end
  end
  