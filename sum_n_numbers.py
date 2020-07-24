#O(1)
def sum1(n):
    return (n)*(n+1)//2

#O(n)
def sum2(n):
    sum = 0
    for i in range(1,n+1):
        sum+=i
    return sum

t = int(input())
while t:
    n = int(input())
    print("sum1 is executed output {}".format(sum1(n)))
    print("sum2 is executed output {}".format(sum2(n)))
    t = t-1