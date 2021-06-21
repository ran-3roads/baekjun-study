a=input().upper()
lis=["ABC","DEF","GHI","JKL","MNO","PQRS","TUV","WXYZ"]
time=0
for i in range(len(lis)):
    for j in lis:
        if(a[i] in j):
            time += lis.index(j) + 3
print(time)