# 1. k번째 약수
'''
    n : 자연수
    k : k번째로 작은 수
'''
# # n, k = input().split()
# n, k = map(int, input().split())
#
# cnt = 0
#
# for i in range(1, n+1):
#     if n%i == 0:
#         cnt +=1
#     if k == cnt:
#         print(k)
#         break
# else: # break를 안당했다 -> k 값이 더 크다
#     print(-1)



# 2. k번째 수
# import sys
#
# T = int(sys.stdin.readline())
# for i in range(T):
#     n, s, e, k = map(int, sys.stdin.readline().split())
#     array = list(map(int, sys.stdin.readline().split()))
#
#     array = array[s-1:e]
#     array.sort()
#     print(f"#{i+1}" ,array[k-1])

# 3. k번째 큰 수

N, K = map(int, input().split())
card = list(map(int, input().split()))
sum = set()

for i in range(0, N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            sum.add(card[i] + card[j] + card[k])

sum = list(sum)
sum.sort(reverse=True)
print(sum[K-1])


