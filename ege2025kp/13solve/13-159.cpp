// Автор: М. Нехорошева

#include <iostream>
#include <bitset>

using namespace std;

int ip(int i1, int i2, int i3, int i4) {
	return i1 << 24 | i2 << 16 | i3 << 8 | i4;
}

int main() {
	int addr = ip(158, 132, 161, 128);
	int mask = ip(255, 255, 255, 128);
	
	int k = 0;
	
	for (int a = 1; a <= ~mask; a += 2) {
		k++;
	}
	
	cout << k << endl;
}
