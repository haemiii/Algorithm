# 1000번

# a, b = map(int, input().split())
# print(a+b)

# 2558번

# a, b = [int(input()) for _ in range(2)]
# print(a + b)

## 다른 방식

# a = int(input())
# b = int(input())
# print(a + b)

# 10950번

# T = int(input())
# for i in range(T):
#     a, b = map(int, input().split())
#     print(a+b)

# 10952번

# while True:
#     a, b = map(int, input().split())
#     if a+b == 0:
#         break
#     else:
#         print(a+b)


# 10953번

# T = int(input())
# for i in range(T):
#     a, b = map(int, input().split(','))
#     print(a+b)

# 11021번

# T = int(input())
# for i in range(T):
#     a, b = map(int, input().split())
#     print(f'Case #{i+1}: {a+b}')

# 11022번

T = int(input())
for i in range(T):
    a, b = map(int, input().split())
    print(f'Case #{i+1}: {a} + {b} = {a+b}')
