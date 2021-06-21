a=int(input())
b=int(input())
c=int(input())
i_res=str(a*b*c)
for i in range(0,10):
    print(i_res.count(str(i)))