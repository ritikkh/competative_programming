def prime(n):
    flag = 0
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            flag = 1
            break
        return flag
    
n,m = input().split()
n = int(n)
m = int(m)
prime1 = []

for i in range(n,m+1):
    if prime(i) == 0:
        prime1.append(i)
        
prime2 = []
for i in prime1:
    for j in prime1:
        cross_prod = int(str(i)+str(j))
        if prime(cross_prod) == 0 and cross_prod not in prime2:
            prime2.append(cross_prod)
        
num1 = (min(prime2))
num2 = (max(prime2))

for i in range(len(prime2)-2):
    sum = num1 + num2
    num1 = num2
    num2 = sum
    
print(prime2,end="")
print(num2)
