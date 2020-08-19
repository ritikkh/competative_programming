n, k = [int(x) for x in input().split()]
c = 0
result = []
samples = [int(x) for x in input().split()]

for i in range(k):
    r1,r2 = [int(x) for x in input().split()]
    for j in samples:
        if ((j >= r1) and (j <= r2)):
            c+=1
    result.append(c)
    c = 0
for i in result:
    print(i,end=" ")