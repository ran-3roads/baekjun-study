T=int(input())
for _ in range(T):
    x1,y1,r1,x2,y2,r2=map(int,input().split())
    d=((x2-x1)**2+(y2-y1)**2)**0.5
    add=r1+r2
    mn=abs(r1-r2)
    if d==0:
        if r1==r2:
            print(-1)
        else:
            print(0)
    else:
        if d==add or d==mn:
            print(1)#내접#외접
        elif d<add and d>mn:
            print(2)#무한대모양
        else:
            print(0)
