'''
실패율 구하기
N : 전체 스테이지의 개수
stages : 사용자가 현재 멈춰있는 스테이지의 번호

실패율 : 스테이지에 도달했으나 아직 클리어하지 못한 플레이어 수 / 스테이지에 도달한 플레이어수
return : 실패율이 높은 스테이지부터 내림차순
'''

'''
import sys

def solution(N, stages):
    # 플레이어수 구하기
    user = len(stages)
    stages.sort()

    not_clear = [0] * N
    for i in stages:
        if 1<= i <= N:
            not_clear[i-1] += 1
    failure = [0] * N
    for i in range(1, N+1):
        failure[i-1] = not_clear[i-1] / user
        user -= not_clear[i-1]

    answer = []
    for i, v in enumerate(failure):
        answer.append([i+1,v])
    answer.sort(key=lambda x : x[1], reverse=True)
    new_answer = []
    for j in answer:
        new_answer.append(j[0])
    return new_answer

'''

def solution(N, stages):
    answer = []
    length = len(stages)

    for i in range(1, N+1):
        count = stages.count(i) # 이런 기능이 있다니...

        if length == 0:
            fail = 0
        else:
            fail = count / length

        answer.append((i ,fail))
        length -= count

    answer = sorted(key= lambda x : x[1], reverse=True)

    answer = [i[0] for i in answer]
    return answer