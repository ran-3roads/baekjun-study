xl=[]
yl=[]
for i in range(3):
    x, y=map(int, input().split())
    xl.append(x)
    yl.append(y)
for j in range(3):
    if xl.count(xl[j])==1:
        a=xl[j]
    if yl.count(yl[j])==1:
        b=yl[j]
print(a,b)
