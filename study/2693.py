T=int(input())
arr=[]
for i in range(T):
    arr.append(list(map(int,input().split())))
    arr[i].sort(reverse=True)
for j in range(T):
    print(arr[j][2])