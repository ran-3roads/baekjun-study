a=int(input())
cnt = 1
d = 6
count = 1
while a > cnt:
    count += 1
    cnt += d
    d += 6
print(count)
# sect=[[0,1],[2,7],[8,19],[20,37],[38,61],[62,70]]
# n=int(input())
# for i in range(0,len(sect)):
#     if sect[i][0]<=n and sect[i][1]>=n:
#         print(i+1)
#         break