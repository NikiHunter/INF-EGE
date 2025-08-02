from fnmatch import fnmatch

for num in range(3023, 10**10, 3023):
    if fnmatch(str(num), "1?954*21"):
        print(num)
