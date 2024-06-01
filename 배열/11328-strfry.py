# 문자 무작위 재배열
n = int(input())
for i in range(n):
    flag = 0
    a, b = input().split()

    a = list(a)
    b = list(b)

    for j in b:
        if j not in a or a.count(j) != b.count(j):
            flag = 1
            break
    if flag == 0:
        print("Possible")
    else:
        print("Impossible")


