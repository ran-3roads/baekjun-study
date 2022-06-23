arr=[]
for _ in range(9):
    n=int(input())
    arr.append(n)
current=sum(arr)-100
arr.sort()

for i in arr:
    a=current-i
    if a in arr:
        arr.remove(i)
        arr.remove(a)
        break

for j in arr:
    print(j)