//Автор И. Свистун
###
uses school;
var x := new CalcIP('158.132.161.128', '255.255.255.128');
x.GenAddrBin.Wh(a -> a[^1]='1').Count.Print;
