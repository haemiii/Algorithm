# 애너그램 관계가 되도록 제거해야하는 최소 개수의 문자 수
from collections import Counter

def min_deletion_to_anagram(word1, word2):

    counter1 = Counter(word1)
    counter2 = Counter(word2)

    all_chars = set(word1) | set(word2)
    deletions = 0

    for char in all_chars:
        deletions += abs(counter1[char] - counter2[char])

    return deletions


word1 = input().strip()
word2 = input().strip()

print(min_deletion_to_anagram(word1, word2))