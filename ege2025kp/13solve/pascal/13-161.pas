//Автор А. Осипов
## 
uses School;
var x := new CalcIP('202.75.38.176', '255.255.255.240');
x.GenAddrBin.Count(t -> not t.IsMatch('000|111')).Println;