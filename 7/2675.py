n=int(input())
res=[]
while n!=0:
    temp=[]
    S = list(map(str, input().split()))
    arr=S[1]
    for i in range(len(arr)):
        for j in range(0,int(S[0])):
            temp.append(arr[i])
    res.append(''.join(temp))
    n=n-1
for i in res:
    print(i)

# best
# t = int(input())
# for k in range(t):
#     r, s = map(str,input().split())
#     for i in range(len(s)):
#         for j in range(int(r)):
#             print(s[i],end="")
#     print()