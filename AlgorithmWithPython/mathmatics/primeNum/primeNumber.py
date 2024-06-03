'''
소수 : 에라토스테네스의 체를 이용하자!
'''
import math

a = 1000
arr = [True for _ in range(a+1)]
arr[1] = False

# 에라토스테네스의 체
for i in range(2, int(math.sqrt(a)) + 1): # 모든 항을 다 돌면 시간초과!
    if arr[i]: # arr[i]가 True : i이전 수들의 배수가 아니였다!
        j = 2
        while i * j <= a:
            arr[i*j] = False # i의 배수를 제거
            j += 1

