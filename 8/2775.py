t=int(input())
res=[]
for i in range(t):
    k=int(input())
    n=int(input())
    resd=[]
    for a in range(1,n+1):
        resd.append(a)
    for r in range(0,k):
        for c in range(1,n):
            resd[c]+=resd[c-1]
    res.append(resd[n-1])
for b in range(len(res)):
    print(res[b])
