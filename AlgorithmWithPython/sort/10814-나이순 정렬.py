n = int(input())
person = [list(input().split()) for _ in range(n)]

person = sorted(person, key= lambda x : int(x[0]))
for i in person:
    print(' '.join(map(str, i)))