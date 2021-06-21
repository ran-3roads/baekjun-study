a = ['c=','c-','dz=','d-','lj','nj','s=','z=']
arr=input()
for i in a:
    arr=arr.replace(i,"$")
print(len(arr))