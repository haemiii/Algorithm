# import sys
#
# n = int(input())
# postfix = list(input())
#
# operand = [] # 피연산자 저장
# stack = []  # 연산 결과값 저장
#
# for i in range(n):
#     operand.append(int(sys.stdin.readline()))
#
# print(operand)
# for j in postfix:
#     if j in "+-*/":
#         a = stack.pop()
#         b = stack.pop()
#         if j == "+":
#             stack.append(b + a)
#         elif j == "-":
#             stack.append(b - a)
#         elif j == "*":
#             stack.append(b * a)
#         elif j == "/":
#             stack.append(b / a)
#     else:
#         stack.append(operand[ord(j) - 65])
#
# print(f'{stack[0]:.2f}')


# 후위 표기식2
import sys
N = int(sys.stdin.readline())
command = list(sys.stdin.readline())
nums = list()

for i in range(N):
    n = int(sys.stdin.readline())
    nums.append(n)

s = list()
for j in command[:-1]:
    if j in '+-*/':
        x = s.pop()
        y = s.pop()
        if j == '+':
            s.append(y+x)
        elif j == '-':
            s.append(y-x)
        elif j =='*':
            s.append(y*x)
        elif j == '/':
            s.append(y/x)
    else:
        i = ord(j) % 65
        s.append(nums[i])

print(f"{s[0]:.2f}")









