a = int(input())
b = int(input())
c = int(input())

multiple = a*b*c
multiple = list(str(multiple))
num = [0]*10
for i in multiple:
    num[int(i)] += 1

for i in num:
    print(i)
