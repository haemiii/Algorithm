s = list(input())
words = [0] * 26

for i in s:
    words[ord(i)-97] += 1

print(' '.join(map(str, words)))