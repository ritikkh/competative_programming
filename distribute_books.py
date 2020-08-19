def countDer(n):
    D = [0]*(n+1)
    D[0] = 1
    D[1] = 0
    D[2] = 1
    for i in range(3, n+1):
        D[i] = (i-1)*(D[i-1]+D[i-2])
    return D[n]
n = int(input())
print(countDer(n)%1000000007)