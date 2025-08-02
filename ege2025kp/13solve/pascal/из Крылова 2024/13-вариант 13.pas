//Автор: И.Свистун
### 
uses School;  
     for var a:=255 downto 0 do
       begin    
  var y:= new CalcIP('127.254.'+a.ToS+'.10', '255.255.224.0');
  var b:=y.GenAddrBin.sel(t -> t.ToS).wh(t -> t[^16:].Cnt('1') <= t[:17].Cnt('1')).cnt;
  if (y.GenAddrBin.cnt=b) then begin print(a); break; end;
  end
  