def jari(x):
    temp=''.join(str(x))
    temp=list(map(int,temp))
    return x+sum(temp)

N=int(input())
res=[]
for i in range(1,N+1):
    if jari(i)==N:
        res.append(i)
if len(res)==0:
    print(0)
else:
    print(min(res))
