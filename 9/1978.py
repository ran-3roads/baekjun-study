def sosu(a):
    if a==1:
        return False
    else:
        for i in range(2,a):
            if a%i==0:
                return False
    return True
cnt=0
n=int(input())
a = list(map(int, input().split()))
for j in range(n):
    if sosu(a[j]):
        cnt+=1
print(cnt)