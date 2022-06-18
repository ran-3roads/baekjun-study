t=int(input())
for _ in range(t):
    n=int(input())
    bin_n=format(n,'b')
    count=0
    for i in bin_n[::-1]:
        if str(i)=="1":
            if len(bin_n)-1==count:
                print(str(count))
            else:
                print(str(count),end=" ")
        count+=1
