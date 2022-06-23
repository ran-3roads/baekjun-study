def solution(N,A,B):
    count_a=[0]*(N+1)
    count_b=[0]*(N+1)
    arr=[]
    sum=0
    for i in range(len(A)):
        count_a[A[i]] += 1
        count_b[B[i]] += 1

    for j in range(1,N+1):
        temp=abs(count_a[j]-count_b[j])
        if temp == 0 and count_a[j]!=0: 
            arr.append(count_a[j]+0.5)
        else :
            arr.append(temp)
    new_arr=sorted(arr)

    for k in range(1,N+1):
        sum=k*abs(new_arr[k])
    return sum
n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
solution(n,a,b)

