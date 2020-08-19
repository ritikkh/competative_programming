from math import sqrt
n,k = input().split()
n = int(n)
k = int(k)

fac = []
for i in range(1,int(sqrt(n))+1):
    if n%i == 0:
        fac.append(i)
        fac.append(n//i)
fac.sort()
if k > len(fac):
    print(1,end='')
else:
    print(fac[-k],end='')