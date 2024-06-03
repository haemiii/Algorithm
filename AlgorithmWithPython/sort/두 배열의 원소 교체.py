import sys

N, K = map(int, sys.stdin.readline().rstrip().split())

arrA = list(map(int, sys.stdin.readline().rstrip().split()))
arrB = list(map(int, sys.stdin.readline().rstrip().split()))

# 1. A는 오름차순 정렬
arrA.sort()

# 2. B는 내림차순 정렬
arrB.sort(reverse=True)

# 3. A <-> B 원소 교체
for i in range(K):
    if arrA[i] < arrB[i]:
        arrA[i], arrB[i] = arrB[i], arrA[i]
    else:
        break
print(sum(arrA))