n=int(input())
arr=str(input())
temp=[]
for i in range(0,n):
    temp.append(arr[i])
temp=list(map(int,temp))#map은 가각
print(sum(temp))
