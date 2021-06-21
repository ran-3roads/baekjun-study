a=int(input())
cnt=1
count=1
d=1
temp=[]
while a >=cnt:
    count += 1
    cnt += d
    d += 1
if (count-1)%2!=0:
    dif=(cnt-1)-a
    temp.append(1+dif)
    temp.append('/')
    temp.append(count-1-dif)
else:
    dif=(cnt-1)-a
    temp.append(count-1-dif)
    temp.append('/')
    temp.append(1+dif)
for i in temp:
    print(i,end='')
