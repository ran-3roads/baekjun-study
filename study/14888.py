def dfs(indx,arr,which,four):
    if which==0:
        arr[indx-1]=arr[indx]+arr[indx-1]
    if which==1:
        arr[indx-1]=arr[indx]-arr[indx-1]
    if which==2:
        arr[indx-1]=arr[indx]*arr[indx-1]
    if which==3 :
        if arr[indx]<0 or arr[indx-1]<0:
            arr[indx-1]=-(abs(arr[indx])//abs(arr[indx-1]))
        else:
             arr[indx-1]=arr[indx]//arr[indx-1]

    if indx==1:
        return res.append(arr[indx-1])

    for j in range(4):
        kfour=four.copy()
        karr=arr.copy()
        if kfour[j]!=0:
            kfour[j]=kfour[j]-1
            dfs(indx-1,karr,j,kfour)

n = int(input())
buf = list(map(int, input().split()))
buf_four = list(map(int, input().split()))
res = []

for k in range(4):
    four=buf_four.copy()
    arr=buf.copy()
    if four[k]!=0:
        four[k]=four[k]-1
        dfs(n-1,arr[::-1],k,four)
print(max(res))
print(min(res))