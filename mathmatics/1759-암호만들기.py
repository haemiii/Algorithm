'''
입력
4 6
a t c i s w
'''

from itertools import combinations

vowels = ('a', 'e', 'i', 'o', 'u')
l, c = map(int, input().split())

words = input().split(' ')
words.sort()
# 순서가 중요! : 조합
for password in combinations(words, l):
    count = 0
    for i in password:
        if i in vowels:
            count += 1
    if 1 <= count <= l-2:
        print(password)
        print(''.join(password))
