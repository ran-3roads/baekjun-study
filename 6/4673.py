nsel=[]
n1=1
while True:
    temp=[]
    res=0
    for i in str(n1):
        temp.append(i)
    temp=list(map(int,temp))
    res=n1+sum(temp)
    if n1>10000:
        break
    nsel.append(res)
    n1=n1+1
for j in range(1,10001):
    if j not in nsel:
        print(j)



