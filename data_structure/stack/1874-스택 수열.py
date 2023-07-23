temp = True
stack = []
op = []
top = 1

N = int(input())
for i in range(N):
    num = int(input())
    while top <= num:
        stack.append(top)
        op.append('+')
        top += 1

    if stack[-1] == num:
        stack.pop()
        op.append('-')

    else:
        temp = False
        break

if temp == False:
    print("NO")
else:
    for i in op:
        print(i)