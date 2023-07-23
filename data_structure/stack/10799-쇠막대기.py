s = list(input())
stack = []
laser = 0
sum = 0

## 66%에서 시간초과!!
# def add_1(n):
#   return n+1

# for i in range(len(s)):
#   if s[i] == "(" and s[i+1] == ")":
    # stack = list(map(add_1, stack)) -> 원인

#   elif s[i] == "(":
#     stack.append(laser)

#   elif s[i] == ")" and s[i-1] != "(":
#     sum += stack.pop() + 1


for i, v in enumerate(s):
    if v == "(":
        stack.append(v)
    elif v == ")":
        if s[i - 1] == "(":
            stack.pop()
            sum += len(stack)
        else:
            stack.pop()
            sum += 1

print(sum)