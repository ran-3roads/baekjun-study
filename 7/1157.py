arr=str(input())
arr_n=[]
for i in range(len(arr)):
    if arr[i].isalpha(): 
        arr_n.append(arr[i].lower())
alp='abcdefghijklmnopqrstuvwxyz'
temp=[]
for i in range(len(alp)):
    temp.append(arr_n.count(alp[i]))
a=max(temp)
if temp.count(a)>1:
    print('?')
else:
    print(alp[temp.index(a)].upper())