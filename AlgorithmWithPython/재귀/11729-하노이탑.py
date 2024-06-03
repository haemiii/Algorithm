# 재귀 : 귀납적 사고를 해야한다!
# 1~n번의 블럭을 이동
# n은 3번 기둥으로 이동해야한다
# 그렇다면 1~n-1번 블록은 모두 2번 기둥에 위치해야함!
# -> 1번기둥 : n번블록, 2번기둥 : 1~n-1번 블록, 3번기둥 : 비어있음
# -> 자기보다 작은 크기의 블록위에 쌓을수 없기때문에 2번기둥에 1~n-1번 블록이 다 있어야한다!

def hanoi(a, b, n):
    if n == 1:
        print(a, end=' ')
        print(b)
        return

    hanoi(a, 6-a-b, n-1)
    print(a, end=' ')
    print(b)
    hanoi(6-a-b, b, n-1)


n = int(input())
print(2**n - 1)
hanoi(1, 3, n)
