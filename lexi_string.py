test = int(input())
while (test > 0):
    p = input()
    s = input()
    
    lst = []
    for i in s:
        lst.append(p.find(i)) 
        
    lst.sort()
    for i in lst:
        print(p[i],end="")
    if test>1:
        print()
    test -= 1