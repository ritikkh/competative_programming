t = int(input())
res = []
for i in range(t):
    arr = []
    n = int(input())
    candy = [int(x) for x in input().split()]
    candy.sort()
    while len(candy) >= 2:
        candy.sort()
        sum1 = (candy[0]+candy[1])
        arr.append(sum1)
        candy.pop(0)
        candy.pop(0)
        candy.append(arr[-1])
    s=0
    for i in arr:
        s+=i
    res.append(s)
for r in res:
    print(r)