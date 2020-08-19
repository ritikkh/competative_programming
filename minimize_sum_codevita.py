n, k = input().split()
cost = []
cost.append(list(map(int,input().rstrip().split())))
arr = cost[0]

for i in range(int(k)):
    maxv = max(arr)
    ind = arr.index(maxv)
    arr[ind] = arr[ind] // 2
sum=0
for i in arr:
    sum+=i
print(sum)
end = time.time()
