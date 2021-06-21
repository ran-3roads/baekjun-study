alp=[]
S=str(input())
for i in range(0,26):
    alp.append(-1)
for j in range(0,len(S)):
    a=ord((S[j]))-97
    if alp[a]==-1:
        alp[a]=j
for k in range(0,26):
    print(alp[k],end=' ')