from itertools import permutations
b = int(input())
a = input()

perm = permutations(a)
r = []
for i in perm:
    str1 = ''
    r.append(int(str1.join(i)))

r = sorted(r)

for i in r:
    if i > int(a):
        print(i)
        break