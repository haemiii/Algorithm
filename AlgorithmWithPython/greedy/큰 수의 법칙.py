'''
입력값

5 8 3
2 4 5 4 6
'''
import sys

input = sys.stdin.readline

n, m, k = map(int, input().split())
numbers = list(map(int, input().split()))

numbers.sort(reverse=True)
sum_value = 0
count = int(m / (k+1)) * k
count += m % (k+1)

sum_value += count * numbers[0]
sum_value += (m-count) * numbers[1]
print(sum_value)

# 해설
first = numbers[0]
second = numbers[1]
result = 0
while True:
    for j in range(k):
        if m == 0:
            break
        result += first
        m -= 1
    if m == 0:
        break
    result += second
    m -= 1