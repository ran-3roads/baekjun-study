N,M=map(int,input().split())
arr=list(map(int,input().split()))
a=len(arr)
res=[]
for i in range(0,a):
    for j in range(i+1,a):
        for x in range(j+1,a):
            if arr[i]+arr[j]+arr[x]<=M:
                res.append(arr[i]+arr[j]+arr[x])
print(max(res))
