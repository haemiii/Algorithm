# 소인수 분해 : 정수를 소수로 구성

'''
   2|72
    ---
   2|36
    ---
   2|18
    ---
   3|9
    ---
   3|3
    ---
     1


=> 2 2 2 3 3
'''

# N = int(input())
#
# arr = [True for _ in range(N+1)]
# arr[1] = False
#
# while True:
#     if N == 1:
#         break
#     for i in range(1, len(arr)):
#         if arr[i] and N % i == 0:
#             N //= i
#             print(i)
#             break

### while + if => 축약 가능!!!

N = int(input())
m = 2

while N != 1:
   if N % m == 0:
       N //= m
       print(m)
   else:
       m += 1
