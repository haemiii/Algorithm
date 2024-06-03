def mod(a, b, m):
    if b == 1:
        return a % m

    val = mod(a, b//2, m)
    val = val * val % m
    if b % 2 == 0:
        return val
    return val * a%m

val = mod(10, 11, 12)
print(val)