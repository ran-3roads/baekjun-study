n,k=map(int,input().split())
arr=list(map(int,input().split()))
count=0 #플러그 빼면 올린다.
plug=[]
for i in range(k):
    if arr[i] in plug:
        continue
    if len(plug)<n:
        plug.append(arr[i])
        continue
    far=0
    temp=0

    for j in plug:
        if j not in arr[i:]:
            temp=j
            break
        elif arr[i:].index(j) > far:
            far=arr[i:].index(j)
            temp=j
    plug[plug.index(temp)]=arr[i]
    count+=1
print(count)