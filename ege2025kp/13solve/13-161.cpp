// Автор: М. Нехорошева

#include <bits/stdc++.h>
using namespace std;
int ip(int i1, int i2, int i3, int i4)
{
	return i1 << 24 | i2 << 16 | i3 << 8 | i4;
}

int main() {
	int addr = ip(202, 75, 38, 176);
	int mask = ip(255, 255, 255, 240);
	int net = addr & mask;
	
	int k = 0;
	
	for (int a = 0; a <= ~mask; ++a) {
		string s = bitset<32>(net | a).to_string();
		
		if (s.find("000") == -1 && s.find("111") == -1) {
			k++;
		}
	}
	
	cout << k << endl;
}
