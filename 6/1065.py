def Han(n):
    res = []
    if (n <= 99):
        for x in range(1,n+1):
            res.append(x)
    else:
        for x in range(1,100):
            res.append(x)
        for x in range(100, n+1):
            a100 = x//100
            a10 = x%100//10
            a1 = x%100%10
            if ((a100-a10) == (a10-a1)):
                res.append(x)
    print(len(res))

n=int(input())
Han(n)