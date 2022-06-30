n,k=map(int,input().split())
arr=list(map(int,input().split()))
res=[]
sum=0
end=0
# start를 증가 시키며 반복
for start in range(n):
    #end를 가능한 만큼 이동
    while sum < k and end < n:
        sum+=arr[end]
        end+=1
    #부분합이 k일때 start와 end거리 재고 res에 추가
    if sum>=k:
        tmp=end-start
        res.append(tmp)
    #start가 한칸 이동하니까 sum에서 현재 start인데스를 가진 arr를 빼줌
    sum-=arr[start]

if len(res)==0:
    print(0)
else:
    print(min(res))