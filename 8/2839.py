n=int(input())
temp=0
while True:
    if n%5==0:
        print(temp+(n//5))
        break
    n=n-3
    temp+=1
    if n<3 and n!=0:
        print(-1)
        break