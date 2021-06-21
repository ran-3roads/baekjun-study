n = int(input())
avg=[]
for i in range(0,n):
    sum=0
    b=0
    arr = list(map(int, input().split()))
    for j in range(1,arr[0]+1):
        sum=sum+arr[j]
    a=sum/arr[0]
    for k in range(1,arr[0]+1):
        if a<arr[k]:
            b=b+1
    avg.append(b/arr[0]*100)
for x in range(0,n):
    print(format(avg[x],".3f")+"%")

