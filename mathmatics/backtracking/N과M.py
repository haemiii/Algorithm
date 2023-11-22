# 15649번 : N과 M

'''
백트래킹 : 모든 경우의 수를 고려!

길이가 M, 1~N까지 자연수 중 중복 x

1. M길이가 되면 다음으로 넘기기
2. 순열의 총 개수는 N* (N+1)
3. 자기자신을 만나면 넘기기

'''

# N, M = map(int, input().split())
# s = list()
#
# def permutation():
#     if len(s) == M:
#         print(' '.join(map(str, s)))
#         return
#
#     for i in range(1, N+1):
#         if i not in s:
#             s.append(i)
#             permutation()
#             s.pop()
#
# permutation()


# 15650번 : N과 M(2)

'''
중복 제거 : (1, 2) = (2, 1)
s[1] > s[0]
'''

# N, M = map(int, input().split())
# s = []
#
# def permutation(k):
#     if len(s) == M:
#         print(' '.join(map(str, s)))
#         return
#
#     for i in range(k, N+1):
#         if i not in s:
#             s.append(i)
#             permutation(i+1)
#             s.pop()
#
# permutation(1)


# 10974번 : 모든 순열

# N = int(input())
# s = []
#
# def permutation():
#     if len(s) == N:
#         print(' '.join(map(str, s)))
#         return
#
#     for i in range(1, N+1):
#         if i not in s:
#             s.append(i)
#             permutation()
#             s.pop()
# permutation()


# 9663번 N-Queen
