a=42
b_arr=[]
cnt=0
for i in range(0,10):
    b=int(input())
    b_arr.append(b%a)
b_arr.sort()
for i in range(1,10):
    if b_arr[i]-b_arr[i-1]==0:
        cnt=cnt+1
res=10-(cnt)
print(res)
