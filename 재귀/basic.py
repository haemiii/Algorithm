def print1ton(n):
    if n == 0:
        return
    print(n)
    return print1ton(n-1)

def sum1ton(n):
    if n == 0:
        return 0
    return n + sum1ton(n-1)

print1ton(5)
print(sum1ton(5))
