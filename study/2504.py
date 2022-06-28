x = list(input())
res = 0
tmp = 1
stack = []
for i in range(len(x)):
    if x[i] == "(":
        stack.append(x[i])
        tmp *= 2
    elif x[i] == "[":
        stack.append(x[i])
        tmp *= 3
    elif x[i] == ")":
        if not stack or stack[-1] == "[":
            res = 0
            break
        if x[i-1] == "(":
            res += tmp
        stack.pop()
        tmp //= 2
    else:
        if not stack or stack[-1] == "(":
            res = 0
            break
        if x[i-1] == "[":
            res += tmp
        stack.pop()
        tmp //= 3
if len(stack)>0:
    print(0)
else:
    print(res)