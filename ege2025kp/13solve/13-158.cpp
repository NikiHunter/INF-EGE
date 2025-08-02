// Автор: М. Нехорошева

#include <iostream>
#include <bitset>

using namespace std;

int ip(int i1, int i2, int i3, int i4) {
	return i1 << 24 | i2 << 16 | i3 << 8 | i4;
}

int main() {
	int addr = ip(192, 168, 248, 176);
	int mask = ip(255, 255, 255, 240);
	int net = addr & mask;
	
	int k = 0;
	
	for (int a = 0; a <= ~mask; ++a) {
		bitset<32> b = net | a;
		if (b.count() > 32 - b.count()) {
			k++;
		}
	}
	
	cout << k << endl;
}
