n=int(input())
res=n
brek=False
for i in range(0,n):
    arr=str(input())
    for j in range(0,len(arr)):
        if brek==True:
            brek=False
            break
        for k in range(j+2,len(arr)):
            if(arr[j]==arr[k] and arr[j]!=arr[j+1]):
                res-=1
                brek=True
                break           
print(res)






