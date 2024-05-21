# 알파벳 정렬 + 최소 한개의 모음 + 최소 두개의 자음
# 모듬의 개수는 1<=x<=2
from itertools import combinations

vowels = ('a', 'e', 'i', 'o', 'u')
l, c = map(int, input().split())
words = list(map(str, input().split()))
words.sort()

for password in combinations(words, l):
    count = 0
    for i in password:
        if i in vowels:
            count += 1
    if 1 <= count <= l-2:
        print(''.join(password))