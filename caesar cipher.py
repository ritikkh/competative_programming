s = input()

e=[]
for i in s:
   e.append(ord(i))


for i in range(len(e)):
    if e[i] == 99:
        e[i] = 112
    if e[i] == 98:
        e[i] = 111
    if e[i] == 97:
        e[i] = 110
    if e[i] == 32:
        e[i] = 32
    else:
        e[i] = e[i] - 3

a = ''
for i in e:
    a += chr(i)
    
print(a)
