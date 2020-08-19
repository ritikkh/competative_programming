n = int(input())
d = []
for i in range(1,int(n**0.5)+1):
    if n%i == 0:
        if i*i == n:
            d.append(i)
        else:    
            d.append(i)
            d.append(n//i)
d.sort()
for i in d:
    print(i,end=" ") 