'''
    ## 가장 큰 수 ##

    자기보다 앞에 있는 수가 작으면 지우고 앞으로 간다.
    -> 스택을 이용하면 편리하다

    5276823 3
    ->7823  /  526

    9977252641 5
    ->99776  / 25241
'''

# N, M = map(int, input().split())
# N = list(map(int, str(N)))
#
# stack = []
# for x in N:
#     while stack and M > 0 and stack[-1] < x:
#         stack.pop()
#         M -= 1
#     stack.append(x)
#
# if M != 0:
#     stack = stack[:-M]
#
# res = ''.join(map(str, stack))
# print(res)


'''
    ## 쇠막대기 ##
    
    ( 가 들어오면 )가 들어올때까지 대기
'''


stick = list(input())
bracket = list()
cnt = 0

for idx, v in enumerate(stick):
    if v == "(":
        bracket.append("(")
    elif v == ")":
        if stick[idx-1] == "(":
            bracket.pop()
            cnt += len(bracket)
        else:
            bracket.pop()
            cnt += 1

print(cnt)