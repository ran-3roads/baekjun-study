import math
a,b = map(int,input().split())
res_gcd=math.gcd(a,b)
res_lcm= (a*b)//res_gcd
print(res_gcd)
print(res_lcm)