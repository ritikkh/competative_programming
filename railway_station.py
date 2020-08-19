arr=[]
dept = []
n = int(input())
for i in range(n):
    x, y = map(int,input().split())
    arr.append(x)
    dept.append(x+y)
arr.sort()
dept.sort()
platforms = 1
result = 1
i = 1
j = 0
while i < n and j < n:
    if arr[i] <= dept[j]:
        platforms+=1
        i+=1
    else:
        platforms-=1
        j+=1
result = max(result, platforms)
print(result)