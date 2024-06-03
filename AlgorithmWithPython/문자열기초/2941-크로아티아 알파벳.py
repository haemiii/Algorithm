words = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
target = input()
cnt = 0

for word in words:
    if word in target:
        cnt += target.count(word)
        target = ' '.join(target.split(word))

target = ''.join(target.split())
print(cnt + len(target))