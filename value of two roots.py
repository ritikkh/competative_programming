a = int(input())
b = int(input())
c = int(input())

det = b*b - 4*a*c
det = pow(det, 0.5)

if det < 0:
    print('root not exist')


ans1 = (b*(-1) - det) / 2*a
ans2 = (b*(-1) + det) / 2*a
print(round(ans1,3), round(ans2,3))

