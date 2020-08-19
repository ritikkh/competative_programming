n = int(input())
l = []

for _ in range(n):
    l.append(int(input().rstrip()))

count = 0
c = []
for i in range(0,len(l)-1,1):
    if l[i] < l[i+1]:
        c.append(count)
        count = 0
    if l[i] > l[i+1]:
        count += 1
        
print(max(c)+1)
