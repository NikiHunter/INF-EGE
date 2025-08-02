//Автор: И.Свистун
### 
uses School;  
     for var a:=255 downto 0 do
       begin    
  var y:= new CalcIP('126.255.'+a.ToS+'.100', '255.255.240.0');
  var b:=y.GenAddrBin.sel(t -> t.ToS).wh(t -> t[^16:].Cnt('1') <= t[:17].Cnt('1')).cnt;
  if (y.GenAddrBin.cnt=b) then begin print(a); break; end;
  end
  