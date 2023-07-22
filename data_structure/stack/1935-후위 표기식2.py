import sys

n = int(input())
postfix = list(input())

operand = [] # 피연산자 저장
stack = []  # 연산 결과값 저장

for i in range(n):
    operand.append(int(sys.stdin.readline()))

print(operand)
for j in postfix:
    if j in "+-*/":
        a = stack.pop()
        b = stack.pop()
        if j == "+":
            stack.append(b + a)
        elif j == "-":
            stack.append(b - a)
        elif j == "*":
            stack.append(b * a)
        elif j == "/":
            stack.append(b / a)
    else:
        stack.append(operand[ord(j) - 65])

print(f'{stack[0]:.2f}')
