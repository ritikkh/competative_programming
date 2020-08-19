n = int(input())
s = input()
q = int(input())
result=[]
for i in range(q):
    p = int(input())
    result.append(s[:p-1].count(s[p-1]))
for i in result:
    print(i)