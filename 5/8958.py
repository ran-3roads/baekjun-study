n = int(input())
check=1
score=[]
for i in range(0,n):
    a=str(input())
    a.upper()
    res=0
    for j in range(len(a)):
        if a[j]=='O':
            res=res+check
            check=check+1
        elif a[j]=='X':
            check=1
    check=1
    score.append(res)
for k in range(len(score)):
    print(score[k])