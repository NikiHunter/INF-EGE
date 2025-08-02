//Автор И. Свистун
### 
uses School;
var x := new CalcIP('202.75.38.176', '255.255.255.240');
x.GenAddrBin.Wh(a -> not a.Contains('111') and not a.Contains('000')).Count.Print;


