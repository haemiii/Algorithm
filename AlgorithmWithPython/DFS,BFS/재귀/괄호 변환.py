# 재귀 -> 최대한 기능을 쪼개서 구현
# 1. 빈 문자열 -> 빈 문자열
# 2. 균형잡힌 괄호 문자열 -> u(더이상 분리 불가능), v(균형잡힌 괄호 문자열)
# 3. u : 올바른 괄호 문자열 -> v(재귀)
# 4. u : 균형잡힌 괄호 문자열 -> 4번 수행

def balanced_index(p):
    count = 0
    for i in range(len(p)):
        if p[i] == '(':
            count += 1
        else:
            count -= 1
        if count == 0:
            return i


def check_proper(u):
    # 올바른 괄호 문자열 -> (())
    count = 0
    for i in u:
        if i == '(':
            count += 1
        else:
            if count == 0:
                return False
            count -= 1
    return True


def solution(p):
    answer = ''
    # 빈 문자열을 반환
    if p == '':
        return p

    # w -> u, v로 분리
    index = balanced_index(p)
    u = p[:index + 1]
    v = p[index + 1:]

    # 올바른괄호 여부
    if check_proper(u):
        answer = u + solution(v)
    else:
        answer = '('
        answer += solution(v)
        answer += ')'
        u = list(u[1:-1])
        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('
        answer += ''.join(u)
    return answer












