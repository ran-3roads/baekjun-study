N=int(input())
data = [['*']*N for _ in range(N)]

def star(N,tN):
    global data
    tN=tN//3
    for i in range(N):
        for j in range(N):
            if (i//tN)%3==1 and (j//tN)%3==1:
                data[i][j]=' '
    if tN==1:
        return
    star(N,tN)

star(N,N)
for i in range(N):
    for j in range(N):
        print(data[i][j], end='')
    print('')
