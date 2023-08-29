# 1. 이분검색 : 로그 n
# -> 정렬되어잇는 자료에만 사용!!!!!!

'''
8 32
23 87 65 12 57 32 99 81
'''

# N, M = map(int, input().split())
# num = list(map(int, input().split()))
# num.sort()
#
# start = 0
# end = N - 1
#
# while start <= end:
#     mid = (start + end) // 2
#     if num[mid] > M:
#         end = mid-1
#     elif num[mid] < M:
#         start = mid + 1
#     else:
#         print(mid+1)
#         break


# 2. 랜선자르기(결정알고리즘) -> 이분탐색을 이용한다!
'''
랜선의 범위는 1 ~~~~~~ 802
              401 -> 2 + 1 + 1 + 1 = 5 : 부족하다 = 길이가 너무 길다
           1 ~~~~~~ 400   
              200 -> 4 + 3 + 2 + 2 : 11 정답!!
입력값 
4 11
802
743
457
539
'''

# K, N = map(int, input().split())
# array = list()
#
# def count(len):
#     cnt = 0
#     for i in array:
#         cnt += (i // len)
#     return cnt
#
# largest = 0
# for i in range(K):
#     tmp = int(input())
#     array.append(tmp)
#     largest = max(tmp, largest)
#
# start = 1
# end = largest
# res = 0
#
# while start <= end:
#     mid = (start + end) // 2
#     if count(mid) >= N:
#         res = mid
#         start = mid+1
#     else:
#         end = mid-1
#
#
# print(res)


# 3. 뮤직비디오

'''
9 3
1 2 3 4 5 6 7 8 9

3개로 분할했을때 최소 용량
- 어떤 값을 기준으로 이진탐색을 할 것인가... -> 최소용량이겠지?
'''

N, M = map(int, input().split())
Music = list(map(int, input().split()))

def Count(capacity):
    cnt = 1
    sum = 0
    for x in Music:
        if sum + x > capacity:
            cnt += 1
            sum = x
        else:
            sum += x
    return cnt

start = 1
end = sum(Music)
res = 0

while start <= end:
    mid = (start + end) // 2
    if Count(mid) <= M:
        res = mid
        end = mid - 1
    else:
        start = mid + 1
print(res)
