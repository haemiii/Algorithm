# a^b를 m으로 나눈 나머지
# a^b mod m

def func1(a, b, m):
    val = 1
    while b > 0:
        val = val * a % m
        b -= 1
    return val

val = func1(6, 100, 5)
print(val)
