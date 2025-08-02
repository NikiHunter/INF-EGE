//Автор И. Свистун
###
uses school;
var x := new CalcIP('211.48.136.64', '255.255.255.224');
x.GenAddrBin.Wh(a -> a[^2:]='11').Count.Print;
