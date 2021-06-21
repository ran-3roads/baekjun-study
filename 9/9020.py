stf=[True for i in range(10001)] #stuff
stf[1]=False
for i in range(2,98):
    for j in range(i*2,10001,i):
        stf[j]=False
T=int(input())
for j in range(T):
    n=int(input())
    a=n//2
    b=a
    for _ in range(n+1):
        if stf[a] and stf[b]:
            print(a,b)
            break
        a-=1
        b+=1
    
            
        

    
# stf=[True for i in range(10001)] #stuff
# stf[1]=False
# res=[]
# for i in range(2,100):
#     for j in range(i*2,10001,i):
#         stf[j]=False

# for x in range(1,len(stf)):
#     if stf[x]!=False:
#         res.append(x)

# T=int(input())
# for j in range(T):
#     temp=[]
#     std=0
#     n=int(input())
#     for q in range(0,len(res)):
#         if res[q]>n:
#             std=q
#             break
#     for d in range(0,std):
#         for f in range(0,std):
#             if n==res[d]+res[f]:
#                 temp.append([res[d],res[f]])
# #     print(temp)
    # if len(temp)!=0:
    #     temp[len(temp)//2].sort()
    #     print("{0} {1}".format(temp[len(temp)//2][0],temp[len(temp)//2][1]))