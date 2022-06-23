def sosu(a):
    if a==1:
        return False
    else:
        for i in range(2,a):
            if a%i==0:
                return False
    return True
res=[]
M=int(input())
N=int(input())
for j in range(M,N+1):
    if sosu(j)!=False:
        res.append(j)
if len(res)==0:
    print(-1)
else:
    print(sum(res))
    print(min(res))