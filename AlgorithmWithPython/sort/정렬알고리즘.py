'''
1. 선택정렬
2. 삽입정렬
3. 퀵 정렬
4. 계수정렬
'''

arr = [2, 5, 1, 3, 6]

# 1. 선택정렬
for i in range(len(arr)):
    min_index = i
    for j in range(i+1, len(arr)):
        if arr[min_index] > arr[j]:
            min_index = j
    arr[min_index], arr[i] = arr[i], arr[min_index]

print(arr)

# 2. 삽입정렬
for i in range(len(arr)):
    for j in range(i, 0,-1):
        if arr[j] < arr[j-1]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
        else:
            break
print(arr)


# 3. 퀵정렬

## 1.
def quick_sort(arr, start, end):
    if start >= end:
        return
    pivot = start
    left = start+1
    right = end

    while left <= right:
        while left <= end and arr[left] <= arr[pivot]:
            left += 1
        while right > start and arr[right] >= arr[pivot]:
            right -= 1

        if left >= right:
            arr[pivot], arr[right] = arr[right], arr[pivot]
        else:
            arr[left], arr[right] = arr[right], arr[left]

    quick_sort(arr, start, right-1)
    quick_sort(arr, right+1, end)

quick_sort(arr, 0, len(arr)- 1)
print(arr)
## 2.

def quick_sort(arr):
    if len(arr) == 1:
        return arr
    pivot = arr[0]
    tail = arr[1:]

    right = [x for x in tail if x >= pivot]
    left = [x for x in tail if x < pivot]

    return quick_sort(left) + [pivot] + quick_sort(right)

print(quick_sort(arr))

# 4. 계수정렬
count = [0] * (max(arr)+1)

for i in arr:
    count[i] += 1

newArr = []
for i in range(len(count)):
    for j in range(count[i]):
        newArr.append(i)

print(newArr)