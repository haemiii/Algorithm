'''
N : 동생의 수
S : 수빈이의 현재 위치
A : 동생들의 위치

이동 범위 : D(S+D, S-D)
D의 최댓값

A들 간의 위치차이 의 최대공약수
'''

N, S = map(int, input().split())
A = list(map(int, input().split()))

A.append(S)
A = sorted(A, reverse=True)

diff = []

for i in range(len(A)-1):
    diff.append(A[i] - A[i+1])
print(diff[-1])
