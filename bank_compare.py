p = int(input())
t = int(input())
bank = []
for i in range(2):
    n = int(input())
    sum1 = 0
    for i in range(n):
        yrs, slab = [float(x) for x in input().split()]
        yrs = int(yrs)
        sq = (1+slab)**(yrs*12)
        emi = (p*(slab))/(1-1/sq)
        sum1 = sum1 + emi
    bank.append(sum1)
if bank[0] < bank[1]:
    print('BANK A', end='')
else:
    print('BANK B', end='')