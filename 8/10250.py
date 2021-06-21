n=int(input())
res=[]
for i in range(n):
    h,w,n=map(int,input().split())

    hosu=n//h+1
    if n%h==0:
        ch=h
        hosu=n//h
    else:
        ch=n%h
    res.append(ch*pow(10,2)+hosu)
for k in res:
    print(k)