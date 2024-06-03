'''
입력값

02984

567
'''
import sys
input = sys.stdin.readline

numbers = list(map(int, input().rstrip()))
sum_value = numbers[0]

for i in range(1, len(numbers)):
    if sum_value == 0 or sum_value == 1 or numbers[i] == 0 or numbers[i] == 1:
        sum_value += numbers[i]
    else:
        sum_value *= numbers[i]

print(sum_value)


##### 해설 #####
for i in range(1, len(numbers)):
    num = numbers[i]
    if num <= 1 or sum_value <= 1:
        sum_value += num
    else:
        sum_value *= num
