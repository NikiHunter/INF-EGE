// Автор: М. Нехорошева

#include <iostream>
#include <bitset>
#include <algorithm>

using namespace std;

int ip(int i1, int i2, int i3, int i4) {
	return i1 << 24 | i2 << 16 | i3 << 8 | i4;
}

int main() {
	int addr = ip(186, 135, 80, 0);
	int mask = ip(255, 255, 252, 0);
	int net = addr & mask;
	
	int k = 0;
	
	for (int i = 0; i <= ~mask; ++i) {
		bitset<32> b = net | i;
		string s= b.to_string();
		string s1=s.substr(0,16);
		string s2=s.substr(16);
		if (count(s1.begin(),s1.end(),'1') > count(s2.begin(),s2.end(),'1')) {
			k++;
		}
	}
	
	cout << k << endl;
}
