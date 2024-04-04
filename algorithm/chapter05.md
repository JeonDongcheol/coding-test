[< 목차 바로 가기](../README.md)

[Chapter 06. 이동 >](./chapter06.md)

# 동빈나 알고리즘 강의 Chapter 05.

> 이진 탐색

## 이진 탐색 알고리즘

- __순차 탐색__ : 리스트 안에 있는 특정한 데이터를 찾기 위해 __앞에서부터 데이터를 하나씩 확인__ 하는 방법

- __이진 탐색__ : _정렬되어 있는 리스트_ 에서 __탐색 범위를 절반씩 좁혀가며 데이터를 탐색__ 하는 방법

    - 이진 탐색은 _시작점_, _끝점_, _중간점_ 을 이용하여 탐색 범위를 설정

### 이진 탐색 동작 예시

이미 정렬된 10개의 데이터 중 값이 4인 원소를 찾는 예시

```
[0] [2] {[4]} [6] [8] [10] [12] [14] [16] [18]
```

__[Step 1]__ (Index 기준) 시작점 : 0, 끝점 : 9, 중간점 : 4 (소수점 이하 제거)

```
  [0] [2] [4] [6] [8] [10] [12] [14] [16] [18]
시작점[0]         중간점[4]                  끝점[9]
```

중간점의 값과 찾으려는 값과 비교하여 찾고자 하는 값보다 중간점 값이 더 크다면, 중간점부터 끝점까지의 값들은 비교할 필요가 없음

따라서, 다시 끝점의 Index를 중간점의 이전 Index로 설정하고, 중간점을 다시 설정하여 탐색 수행

__[Step 2]__ 시작점: 0, 끝점 : 3, 중간점 : 1 (소수점 이하 제거)

```
  [0]     [2]     [4]     [6] ... (이후 Skip)
시작점[0] 중간점[1]         끝점[3]
```

중간점의 값과 찾으려는 값과 비교했을 때 찾고자하는 값이 중간점의 값보다 크기 때문에, 중간점 이전 Index의 값들은 비교할 필요가 없음

따라서, 시작점의 Index를 중간점 다음 Index로 설정

__[Step 3]__ 시작점 : 2, 끝점 : 3, 중간점 : 2 (소수점 이하 제거)

```
...   [4]     [6]   ...
    시작점[2] 끝점[3]
    중간점[2]
```

찾으려는 값이 시작점(중간점)의 값과 동일하기 때문에 더 이상 탐색을 수행하지 않음

### 이진 탐색의 시간 복잡도

단계마다 탐색 범위를 2로 나누는 것과 동일하므로 연산 횟수는 __log2 N에 비례__

예를 들어, 초기 데이터 개수가 32개일 때, 이상적으로 1단계를 거치면 16개 가량의 데이터만 남음

2단계에서는 8개, 3단계에서는 4개 가량의 데이터만 남음

-> 이진 탐색은 탐색 범위를 절반씩 줄이며, 시간 복잡도는 __O(logN)__ 을 보장

### 이진 탐색 소스코드 : 재귀적 구현

```python
# 이진 탐색 소스코드 구현 (재귀 함수)
def binary_search(array, target, start, end):
    # 탐색하고자 하는 범위에 데이터가 없다는 의미이므로 None 반환
    if start > end:
        return None

    # 시작Index와 끝Index를 더한 다음에 2로 나눈 몫을 설정하면 중간 Index 설정 가능
    mid = (start + end) // 2

    # 찾은 경우 중간점 Index 반환
    if array[mid] == target:
        return mid
    # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
    else:
        return binary_search(array, target, mid + 1, end)

# N(원소의 개수)과 Target(찾고자 하는 값)을 입력 받기
n, target = list(map(int, input().split()))

# 전체 원소 입력 받기
array = list(map(int, input().split()))

# 이진 탐색 수행 결과 출력
result = binary_search(array, target, 0, n - 1)

# 위치(Index) 출력
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result + 1)
```

### 이진 탐색 소스코드 : 반복문 구현

```python
# 이진 탐색 소스코드 구현 (반복문)
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        # 찾은 경우 중간점 Index 반환
        if array[mid] == target:
            return mid
        # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
        elif array[mid] > target:
            end = mid - 1
        # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
        else:
            start = mid + 1

    return None

# N(원소의 개수)과 Target(찾고자 하는 값)을 입력 받기
n, target = list(map(int, input().split()))

# 전체 원소 입력 받기
array = list(map(int, input().split()))

# 이진 탐색 수행 결과 출력
result = binary_search(array, target, 0, n - 1)

# 위치(Index) 출력
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result + 1)
```

### Python 이진 탐색 라이브러리

- bisect_left(a, x) : 정렬된 순서를 유지하면서 배열 a에 x를 삽입할 __가장 왼쪽 Index__ 를 반환

- bisect_right(a, x) : 정렬된 순서를 유지하면서 배열 a에 x를 삽입할 __가장 오른쪽 Index__ 를 반환

```
[1]     [2]     [4]     [4]     [8]
             ^               ^
     bisect_left(a,4)  bisect_right(a,4)
```

```python
from bisect import bisect_left, bisect_right

a = [1, 2, 4, 4, 8]
x = 4

print(bisect_left(a, x)) # 2
print(bisect_right(a, x)) # 4
```

### 값이 특정 범위에 속하는 데이터 개수 구하기

```python
from bisect import bisect_left, bisect_right

# 값이 [left_value, right_value]인 데이터 개수를 반환하는 함수
def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)

    return right_index - left_index

a = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]

# 값이 4인 데이터 개수 출력
print(count_by_range(a, 4, 4))

# 값이 [-1, 3] 범위에 있는 데이터 개수 출력
print(count_by_range(a, -1, 3))
```

### 파라메트릭 서치(Parametric Search)

_최적화 문제_ 를 __결정문제__ ('예' 혹은 '아니오')로 바꾸어 해결하는 기법

ex) 특정한 조건을 만족하는 가장 알맞은 값을 빠르게 찾는 최적화 문제

일반적으로 코딩 테스트에서 파라메트릭 서치 문제는 __이진 탐색__ 을 이용하여 해결 가능

## 이진 탐색 문제풀이

### 예시 1) 떡볶이 떡 만들기



---

## Reference.

- [동빈나 Youtube : 이코테 2021 5장](https://youtu.be/94RC-DsGMLo?feature=shared)