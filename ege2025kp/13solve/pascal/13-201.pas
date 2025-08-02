//Автор: И.Свистун
### 
uses School;  
     for var z:=255 downto 0 do
       begin    
  var y:= new CalcIP('227.31.'+z.ToS+'.139', '255.255.255.224');
  var b:=y.GenAddrBin.sel(t -> t.ToS).wh(t -> t[^16:].Cnt('0') >= t[:17].Cnt('0')).cnt; 
  if (y.GenAddrBin.cnt=b) then begin print(z);break; end;
  end
  