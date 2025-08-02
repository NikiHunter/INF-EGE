//Автор: И.Свистун
### 
uses School;  
     for var z:=255 downto 0 do
       begin    
  var y:= new CalcIP('250.113.'+z.ToS+'.197', '255.255.255.192');
  var b:=y.GenAddrBin.sel(t -> t.ToS).wh(t -> t[^16:].Cnt('1') <= t[:17].Cnt('1')).cnt; 
  if (y.GenAddrBin.cnt=b) then begin print(z);break; end;
  end
  