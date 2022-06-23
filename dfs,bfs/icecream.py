def dfs(x,y):
    if x<=-1 or x>=n or y<=-1 or y>=m: #0이하면 안되게하자
        return False
    if graph[x][y]==0: #four -1 
        graph[x][y]=1
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    return False


n,m = map(int,input().split())

graph=[]
for i in range(n):
    graph.append(list(map(int,input())))

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            result +=1
print(result)