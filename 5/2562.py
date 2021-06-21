arr=[]
for i in range(0,9):
    n=int(input())
    arr.append(n)
max=arr[0]
cnt=0
for i in range(0,9):
    if max<=arr[i]:
        max=arr[i]
        cnt=i+1
print(max)
print(cnt)

