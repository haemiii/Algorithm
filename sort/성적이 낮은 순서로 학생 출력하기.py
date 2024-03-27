import sys

# input = sys.stdin.readline()
N = int(sys.stdin.readline())

# 입력값 받기
arr = [sys.stdin.readline().rstrip().split() for _ in range(N)]

# 정렬
arr = sorted(arr, key=lambda x: x[1])

# 출력
for i in arr:
    print(i[0], end=" ")
