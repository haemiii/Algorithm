## 시간초과!!!

# N = int(input())
# A = list(map(int, input().split()))
#
# s = []
# for i in range(N):
#     for j in range(i+1,N):
#         if A[i] < A[j]:
#             s.append(A[j])
#             break
#         if j == N-1:
#             s.append(-1)
# s.append(-1)
# print(' '.join(map(str, s)))

'''
5
6 5 4 3 7
'''
N = int(input())
A = list(map(int, input().split()))
answer = [-1] * N
stack = []

stack.append(0)
for i in range(1, N):
    while stack and A[stack[-1]] < A[i]:
        answer[stack.pop()] = A[i]
    stack.append(i)

print(*answer)