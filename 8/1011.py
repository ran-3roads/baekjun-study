T= int(input())

for _ in range(T):
    x, y = map(int,input().split())
    distance = y - x
    cnt = 0 
    move = 1 
    std = 0
    while std < distance :
        cnt += 1
        std += move
        if cnt % 2 == 0 :
            move += 1  
    print(cnt)



# n= int(input())
# for c in range(n):
#     A,B=map(int,input().split())
#     leng=B-A
#     temp=[]
#     i=1
#     while True:
#         temp.append(i-1)
#         if  0<leng-(i+sum(temp)*2)<=i:
#             print((temp))
#             print(len(temp)*2)
#             break
#         elif leng-(i+sum(temp)*2)<=0:
#             print(temp)
#             print(len(temp)*2-1)
#             break
#         i+=1