from itertools import *
from math import *
from ipaddress import *
from functools import *
from sys import *
from turtle import *
from string import *

#1
print(*range(1, 9))
r = 'AB AE AH BH CG CD CE DF EG GF FH'.split()
t = '247 147 578 126 38 47 136 235'.split()
for p in permutations('ABCDEFGH'):
   if all(str(p.index(y)+1) in t[p.index(x)] for x,y in r):
       print(*p)


#2
def f(x,y,z,w):
   return z or (z == w) or not (y <= x)
##
for a1,a2,a3,a4,a5,a6,a7 in product([0,1], repeat = 7):
   t = [(a1,a2,0,1),
        (a3,1,a4,0),
        (a5,0,a6,a7)]
   if len(t) != len(set(t)): continue
   for p in permutations('xyzw'):
       if [f(**dict(zip(p,r))) for r in t] == [0,0,0]:
           print(*p)
print('x y z w')
for x in range(2):
   for y in range(2):
       for z in range(2):
           for w in range(2):
               if f(x,y,z,w) == 0:
                   print(x,y,z,w)


#5
def tr(x, q=3):
    a = ''
    while x >0 :
        a += str(x%q)
        x //= q
    return a[::-1]
ans = []
for n in range(1, 5_000):
   r = tr(n)
   if n % 3 == 0:
       r += r[-2:]
   else:
       k = (n%3) * 5
       r += tr(k)
   r = int(r, 3)
   if r >= 290:
       print(n)
       break
       ans.append(r)
        
print(min(ans))

#6
k = 10
lt (90)
screensize(10_000, 10_000)
tracer(0)
for _ in range(2):
   fd(24*k)
   rt(90)
   fd(20*k)
   rt(90)
up()
fd(7*k)
rt(90)
fd(7*k)
lt(90)
down()

for _ in range(2):
   fd(30*k)
   rt(90)
   fd(27*k)
   rt(90)

update()
tracer(0)
up()
for x in range(40):
   for y in range(40):
       goto(x*k, y*k)
       dot(3, 'red')

update()
done()
            

#7
Q1 = 1920 * 1080 * 22 * 120
Q2 = 1280 * 1024 * 21 * 120
print((Q1 - Q2) / 2**13)


#8
ans = []
alf = sorted(set('ВЕНЕРА'))
k = 0
for x1 in product(alf, repeat = 5):
   x = ''.join(x1)
   k += 1
   if x[0] != 'Н' and x.count('В') == 2 and k % 2 != 0:
       ans.append([k, x])
print(max(ans))
    

#9
f = open('9-251.csv')
a = [tuple(map(int, x.split(';'))) for x in f]

ans = []
for x in a:
   k = sorted([x.count(y) for y in set(x)])
   if k == [1,1,1,3]:
       r = [y for y in set(x) if x.count(y) == 3]
       n = [y for y in set(x) if x.count(y) == 1]
       if r[0] < 2*min(n):
           ans.extend(x)
print(sum(ans)/len(ans))
        
#11
Q1 = I * 3410
Q11 = ceil(14*2**33 / 2984523)
I = Q11 / 3410
print(I)
print(ceil((12*3410)/8) * 2984523 / 2**30)
print(2**11+1)

for N in range(1, 10**12):
   I = ceil(log2(N))
   Q1 = ceil (I * 3410 / 8)
   Qn = Q1 * 2984523 / 2**30
   if Qn >= 14:
       print(N)
       break
#12

#13
ip = ip_address('186.215.243.5')
m = ip_address('255.255.192.0')
net = [x for x in ip_network(f'{ip}/{m}', 0)]
print(str(net[-2]).replace('.', ''))

#14
l = ascii_uppercase
num = range(10, 36)
print(*zip(num, l))
alf = printable[:27]

p = 27
for x in alf:
   a1 = int(f'2107{x}792', 27)
   a2 = int(f'565{x}211', 27)
   a = a1 + a2
   if a % 26 == 0:
       print(x, a // 26)
       break
        
        
#15
def f(x,a):
   return ()

for a in range(0, 2000):
   if all(f(x,a) for x in range(0, 2000) for y in range(0, 2000) ):
       print(a)
       break


#16
setrecursionlimit(10**4)
@lru_cache()
def f(n):
   if n == 1: return 1
   else: return n**2 + f(n-1)

print(f(2025) - f(2022))

f = [0] * 2030
f[1] = 1
for n in range(2, 2030):
   f[n] = n**2 + f[n-1]

print(f[2025] - f[2022])

#17
f = open('17.txt')
a = [int(x) for x in f]
m13 = max([x for x in a if abs(x) % 100 == 13])

r = range(10**4, 10**5)
ans = []
for i in range(len(a) - 2):
   x,y,z = a[i:i+3]
   if (abs(x) in r)+(abs(y) in r)+(abs(z) in r) == 2 and \
      x+y+z <= m13:
       ans.append(x+y+z)
print(len(ans), max(ans))

#19-21
def f(s,m):
   if s <= 11: return m%2 == 0
   if m <0 : return 0

   h = [f(s-1, m-1), f(s-3, m-1)]

   if (m-1)%2==0: return any(h)
   else: return all(h)

##print(19, min([s for s in range(12, 1000) if f(s,2)]))
print(20, ([s for s in range(12, 1000) if f(s,3) and not f(s,1)]))
print(21, ([s for s in range(12, 1000) if f(s,4) and not f(s,2)]))

#23
def f(s,e,p):
   if s < e or 17 in p: return 0
   if s == e and 27 in p and 75 in p: return 1
   return f(s-3,e,p+[s-3]) + f(s//3,e,p+[s//3])

print(f(81, 3, [81]))

#24
s = open('24.txt').readline()
r = n = m = 0
l = s.index('D')

for r in range(l+1, len(s)):
   if s[r] in '0123456789': n += 1
   if s[r] == 'D':
       l = r
       n = 0

   while n > 50 or s[l] != 'D':
       if s[l] in '0123456789': n -= 1
       l += 1

   if n == 50:
       m = max(m, r - l + 1)

s = s.replace('D', ' D')
a = [x for x in s.split() if x[0] == 'D' and sum(x.count(i) for i in '0123456789') == 50]
m = max(a, key = len)
print(len(m), m)


#25
def isprime(x):
   return x > 1 and all(x % k != 0 for k in range(2, int(x**0.5)+1))

def div(x):
   d = set()
   for k in range(2, int(x**0.5)+1):
       if x % k == 0:
           if isprime(k) and str(k).count('0') == 1 \
              and isprime(x//k) and str(x//k).count('0') == 1:
               d.add(k)
               d.add(x//k)
               break
   return sorted(d)

c = 0
for x in range(2_900_001, 10**18):
   d = div(x)
   if d != []:
       print(x, max(d))
       c += 1
   if c == 5: break
    
#26
f = open('26-test.txt')
n, m = map(int, f.readline().split())

box = []
for i in range(m):
   x,y = map(int, f.readline().split())
   box.append((x,0))
   box.append((y,1))
for i in range(n-m):
   x= int(f.readline())
   box.append((x,0))

box.sort(reverse = 1)
d = [box[0]]
for x in box:
   r, t = x
   if d[-1][0] - r >= 5 and d[-1][1] != t:
       d.append(x)
##print(d)
print(len(d), d[-1][0])
    


#27
f = open('27A_18677.txt')
a = map(int, f.readline().split())
a = [tuple(map(float, p.replace(',','.').split())) for p in f]

cl = []
while a:
   cl.append([a.pop(0)])
   for p in cl[-1]:
       for p1 in a:
           if dist(p, p1) <= 1:
               cl[-1].append(p1)
               a.remove(p1)

print([len(k) for k in cl])

cl = [k for k in cl if len(k) > 100]  # УДАЛЯЕМ НЕНУЖНЫЕ ТОЧЕЧКИ

def cent(k):
   min_point = 10**18
   for p in k:
       cs = 0
       for p1 in k:
           cs += dist(p,p1)
       if cs < min_point:
           min_point = cs
           the_point = p
   return the_point

c = []
for k in cl:
   c.append(cent(k))

px = sum(i[0] for i in c)/len(c)
py = sum(i[1] for i in c)/len(c)

print(int(abs(px) * 100_000), int(abs(py) * 100_000))
    



















