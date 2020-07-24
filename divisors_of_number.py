from math import *
#O(n)
def func1(n):
    div1 = []
    for i in range(1, n+1):
        if n % i == 0:
            div1.append(i)
    return div1
#O(sqrt(n))
def func2(n):
    div2 = set()
    for i in range(1,int(sqrt(n)+1)):
        if n%i == 0:
            div2.add(i)
            div2.add(n//i)
    return list(div2)

t = int(input())
while t:
    n = int(input())
    div1 = func1(n)
    print(*div1)
    
    div2 = func2(n)
    print(*div2)
    t = t - 1