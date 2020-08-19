car = int(input())
D = {}
collision=0
for i in range(car):
    x,y,speed = input().split()
    x = int(x)
    y = int(y)
    speed = int(speed)
    sq_time = (x**2 + y**2)/(speed**2)
    if (D.get(sq_time)==None):
        D[sq_time]=1
    else:
        D[sq_time] = D[sq_time] + 1
         
for keys in D:
    if(D[keys]!=1):
        collision=collision+(D[keys]*(D[keys]-1))/2
print(int(collision))