# # () 괄호
# # ( : 스택에서 대기
# # ) : ( -> 괄호를 제거 시켜줌 -> 짝을 맞추는 것!
#
# # 스택에 ( 가 남아있거나 스택에 아무것도 없는데 ) 입력이 들어오면 에러!
#
# n = int(input())
#
# for i in range(n):
#     stack = []
#     e = 0
#     ps = list(input())
#
#     for j in ps:
#         if j == "(":
#             stack.append(j)
#         else:
#             if len(stack) == 0:
#                 e = 1
#                 break
#             stack.pop()
#     if e == 1 or len(stack) != 0:
#         print("NO")
#     else:
#         print("YES")

# 괄호
import sys
T = int(input())

for i in range(T):
    b = list(sys.stdin.readline())
    s = list()

    for j in b[:-1]:
        if j == '(':
            s.append(j)
        else:
            if len(s) == 0:
                s.append(-1)
                break
            s.pop()
    if len(s) == 0:
        print("YES")
    else:
        print("NO")





















