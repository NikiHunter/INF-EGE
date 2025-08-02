def solution_105():
	return 2**(24*2**23//131072//128)


def solution_118():
	return 4*2**20//65536-ceil(ceil(log2(26))*15/8)-ceil(ceil(log2(2023))*20/8)