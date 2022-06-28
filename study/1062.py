import sys

def dfs(index,cnt,alph,words):
    global result
    if cnt == k-5:
        tmp=0
        for word in words:
            check = True
            for w in word:
                if not alph[ord(w)-ord('a')]:
                    check=False
                    break
            if check==True:
                tmp+=1
        result = max(tmp,result)
        return
    for i in range(index,26):
        if not alph[i]:
            alph[i]=True
            dfs(i,cnt+1,alph,words)
            alph[i]=False

n, k = map(int, input().split())

if k<5:
    print(0)
    sys.exit()
elif k==26:
    print(n)
    sys.exit()

words = [set(input().rstrip()[4:-4]) for _ in range(n)]
alph = [False] * 26


result=0
alph[ord('a')-ord('a')]=True
alph[ord('n')-ord('a')]=True
alph[ord('t')-ord('a')]=True
alph[ord('i')-ord('a')]=True
alph[ord('c')-ord('a')]=True

dfs(0,0,alph,words)
print(result)