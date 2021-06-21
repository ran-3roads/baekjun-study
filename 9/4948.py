def sosu(a):
    for i in range(2,int(a**0.5)+1):
        if a%i==0:
            return False
    return True
stuff=list(range(2,2*123456))
res=[]
for x in stuff:
    if sosu(x)!=False:
        res.append(x)
while True:
    n=int(input())
    if n==0:
        break
    cnt=0
    for j in res:
             if n<j<=n*2:
                cnt += 1
    print(cnt)
