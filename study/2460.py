arr=[]
for i in range(10):
    a,b=map(int,input().split())
    if i==0:
        arr.append(b)
    else:
        n=arr[i-1]+b-a
        arr.append(n)
print(max(arr))