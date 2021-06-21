n = int(input())
arr = list(map(int, input().split()))
arr.sort()
max=arr[n-1]
avg=0
for i in range(0,n):
    arr[i]=arr[i]/max*100
    avg=avg+arr[i]
print(avg/n)