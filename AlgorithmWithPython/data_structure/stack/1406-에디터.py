'''
|a|b|c|d
'''

## 시간초과!

import sys
#
# s = list(sys.stdin.readline())
# M = int(sys.stdin.readline())
# cursor = len(s)
#
# for i in range(M):
#     command = list(sys.stdin.readline().split())
#
#     if command[0] == 'L':
#         if cursor != 0:
#             cursor -= 1
#     elif command[0] == 'D':
#         if cursor != len(s):
#             cursor += 1
#     elif command[0] == 'B':
#         if cursor != 0:
#             s = s[:cursor-1]+s[cursor:]
#             cursor -= 1
#     elif command[0] =='P':
#         s.insert(cursor, command[1])
#         cursor += 1
# print(''.join(map(str, s)))

## 커서를 기준으로 스택을 둘로 나눈다!
st1 = list(sys.stdin.readline().strip())
st2 = []

m = int(sys.stdin.readline())
for _ in range(m):
    command = list(sys.stdin.readline().split())
    print(command)

    if command[0] == 'L':
        if st1:
            st2.append(st1.pop())
    elif command[0] == 'D':
        if st2:
            st1.append(st2.pop())
    elif command[0] == 'B':
        if st1:
            st1.pop()
    else:
        st1.append(command[1])
print("".join(st1 + list(reversed(st2))))