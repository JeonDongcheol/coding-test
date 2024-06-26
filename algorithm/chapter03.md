[< 목차 바로 가기](../README.md)

[Chapter 04. 이동 >](./chapter04.md)

# 동빈나 알고리즘 강의 Chapter 03.

> DFS & BFS

## 그래프 탐색 알고리즘: DFS/BFS

__탐색(Search)__ 이란, 많은 양의 데이터 중에서 __원하는 데이터, 해당 데이터의 위치를 찾는 과정__

대표적인 그래프 탐색 알고리즘으로는 DFS/BFS가 있는데, 이는 코딩 테스트에서 매우 자주 등장하는 유형

* 특히 국내 대기업 공채에서는 이를 자주 활용한 문제가 나옴

## 스택(Stack) 자료구조

__먼저 들어온 데이터가 나중에 나가는 형식(선입후출)__ 의 자료구조로, __입구와 출구가 동일한 형태__ 로 스택을 시각화 할 수 있음

예시) 박스 쌓기 예시 - 여러 개의 박스를 쌓을 때 차례대로 쌓고 내릴 때는 위에서부터(나중에 쌓은 박스부터) 내림

스택 자료구조는 DFS뿐만 아니라 다른 다양한 알고리즘에서도 사용

- 스택 자료구조의 연산
    - 삽입
    - 삭제

파이썬에서는 __List__ 객체를 기반으로 Stack을 구현

```python
stack = []

# append, pop 메소드는 시간 복잡도가 O(1)이기 때문에 stack을 사용하기에 적합
stack.append(5) # 삽입(5)
stack.append(2) # 삽입(2)
stack.append(3) # 삽입(3)
stack.append(7) # 삽입(7)
stack.pop() # 삭제 : 가장 나중에 들어온 원소 7 삭제
stack.append(1) # 삽입(1)
stack.append(4) # 삽입(4)
stack.pop() # 삭제 : 가장 나중에 들어온 원소 4 삭제

print(stack[::-1]) # 최상단 원소부터 출력 [1, 3, 2, 5]
print(stack) # 최하단 원소부터 출력 [5, 2, 3, 1]
```

---

## 큐(Queue) 자료구조

__먼저 들어온 데이터가 먼저 나가는 형식(선입선출)__ 의 자료구조로, __입구와출구가 모두 뚫려 있는 터널과 같은 형태__ 로 시각화 할 수 있음

예시) 은행 창구에서 번호표를 뽑고 먼저 뽑은 순서대로 빠져나가는 형식

```python
# Deque 라이브러리는 Stack과 Queue의 장점을 합친 라이브러리
from collections import deque

# 큐(Queue) 구현을 위해 deque 라이브러리 사용
queue = deque() # Deque 객체 생성

# append, popleft는 모두 O(1)의 시간 복잡도를 가짐
queue.append(5) # 삽입(5)
queue.append(2) # 삽입(2)
queue.append(3) # 삽입(3)
queue.append(7) # 삽입(7)
queue.popleft() # 삭제 : 가장 처음에 들어온 원소 5 삭제
queue.append(1) # 삽입(1)
queue.append(4) # 삽입(4)
queue.popleft() # 삭제 : 두 번째로 들어온 원소 2 삭제

print(queue) # 먼저 들어온 순서대로 출력 deque([3, 7, 1, 4])
queue.reverse() # 역순으로 바꾸기
print(queue) # 나중에 들어온 원소부터 출력 deque([4, 1, 7, 3])
```

Queue를 구현할 때는 기본적으로 제공하는 List 객체보다는 Deque를 이용하는 것이 훨씬 좋음

---

## 재귀 함수(Recursive Function)

재귀 함수란 __자기 자신을 다시 호출하는 함수__

예시)

- '재귀 합수를 호출합니다'라는 문자열을 무한히 출력
- 어느 정도 출력하다가 최대 재귀 깊이 초과 메시지 출력 (Python에는 최대 재귀 깊이 초과가 존재)

```python
# Stack 안에 차례대로 Recursive Function이 쌓임
def recursive_function():
    print('재귀 함수를 호출합니다.')
    recursive_function()

recursive_function()
```

### 재귀 함수의 종료 조건

재귀 함수를 문제 풀이에서 사용할 때는 재귀 함수의 __종료 조건을 반드시 명시__

종료 조건을 제대로 명시하지 않으면 함수가 무한히 호출

예시)

```python
def recursive_function(i):
    # 100번째 호출을 했을 때 종료되도록 조건 명시
    if i == 100:
        return

    print(i, '번째 재귀함수에서', i+1, '번째 재귀함수를 호출합니다.')
    recursive_function(i+1)
    print(i, '번째 재귀함수를 종료합니다.')

recursive_function(1)
```

### 재귀 함수 예시 1) 팩토리얼 구현

n! = 1 * 2 * 3 * 4 * ... * (n-1) * n

수학적으로 0!과 1!의 값은 1

```python
# 기존의 반복적으로 구현한 n!
def factorial_iterative(n):
    result = 1

    # 1부터 n까지의 수를 차례대로 곱하기
    for i in range(1, n+1):
        result *= i

    return result

# 재귀함수 기반 재귀적으로 구현한 n!
def factorial_recursive(n):
    # n이 1 이하인 경우 1을 반환
    if n <= 1:
        return 1

    # n! = n * (n-1)!을 그대로 코드로 작성
    return n * factorial_recursive(n-1)

# 각각의 방식으로 구현한 n! 출력 (n = 5)
print('반복적으로 구현 : ', factorial_iterative(5)) # 120
print('재귀적으로 구현 : ', factorial_recursive(5)) # 120
```

### 재귀 함수 예시2) 최대공약수 계산(유클리드 호제법 기반)

__두 개의 자연수에 대한 최대공약수(두 수의 공통된 약수 중 가장 큰 값)__ 를 구하는 대표적인 알고리즘으로는 __유클리드 호제법__ 이 있음

- 유클리드 호제법 : 두 자연수 A, B에 대하여 (A > B) A를 B로 나눈 나머지를 R이라고 할 때, 이 때 A와 B의 최대공약수는 B와 R의 최대공약수와 같음

유클리드 호제법을 이용한 재귀 함수 작성 방법

예) GCD(192, 162) : 6

|단계|A|B|
|:---:|:---:|:---:|
|1|192|162|
|2|162|30|
|3|30|12|
|4|12|6|

```python
def gcd(a, b):
    # a와 b를 나눈 나머지가 0이라면, b를 반환
    if a % b == 0:
        return b
    # 0이 아니라면 재귀적으로 함수 호출
    else:
        return gcd(b, a % b)

print(gcd(192, 162)) # 6
```

### 재귀 함수 사용의 유의 사항

- 재귀 함수를 잘 활용하면 점화식 형태의 복잡한 알고리즘을 간단한 형태로 작성 가능하지만, 반대로 다른 사람이 이해하기 어려운 코드가 될 수 있기 때문에 신중하게 사용
- 모든 재귀 함수는 __반복문을 이용해 동일한 형태로 구현이 가능__
- 재귀 함수가 반복문보다 항상 유리하지는 않음 (반드시 더 좋은 방법을 고민한 뒤에 풀어야 함)
- 컴퓨터가 함수를 연속적으로 호출하면 컴퓨터 메모리 내부의 Stack Frame에 쌓이는데, 그래서 스택을 사용해야할 때 구현상 __스택 라이브러리 대신에 재귀 함수를 이용__ 하는 경우가 많음 (ex. DFS의 간결한 구현)

---

## DFS (Depth-First Search)

DFS는 __깊이 우선 탐색__ 이라고 부르며, 그래프에서 __깊은 부분을 우선적으로 탐색하는 알고리즘__

DFS는 __스택 자료구조(혹은 재귀함수)__ 를 이용

- DFS의 동작 과정

    1. 탐색 시작 노드를 스택에 삽입하고 방문 처리
    2. 스택의 최상단 노드에 방문하지 않은 인접한 노드가 하나라도 있으면, 그 노드를 스택에 넣고 방문 처리.
    3. _방문하지 않은 인접 노드가 없다면_, 스택에서 최상단 노드를 꺼냄
    4. 더 이상 2번의 과정을 수행할 수 없을 때까지 반복

예시)

![Alt Text][03_dfs_graph_01]

__[Step 0]__ 그래프 준비 : 시작 노드 1

- 방문 기준 : __번호가 낮은 인접 노드__ 부터 방문

__[Step 1]__ 시작 노드인 '1'을 스택에 삽입하고 방문 처리 : `[1]`

__[Step 2]__ 스택의 최상단 노드인 '1'에 방문하지 않은 인접 노드 2, 3, 8이 있는데, 이 중에서 가장 작은 노드인 '2'를 스택에 넣고 방문 처리 : `[1, 2]`

__[Step 3]__ 스택의 최상단 노드인 '2'에 방문하지 않은 인접 노드 7이 있기 때문에, '7'을 스택에 넣고 방문 처리 : `[1, 2, 7]`

__[Step 4]__ 스택의 최상단 노드인 '7'에 방문하지 않은 인접 노드 6, 8이 있는데, 이 중에서 가장 작은 노드인 '6'을 스택에 넣고 방문 처리 : `[1, 2, 7, 6]`

__[Step 5]__ 스택의 최상단 노드인 '6'에 방문하지 않은 인접 노드가 없기 때문에, 스택에서 '6'을 꺼냄 : `[1, 2, 7]`

__[Step 6]__ 스택의 최상단 노드인 '7'에 방문하지 않은 인접 노드 8이 있기 때문에, '8'을 스택에 넣고 방문 처리 : `[1, 2, 7, 8]`

- 해당 과정을 반복하였을 때 __전체 노드의 탐색 순서(스택에 들어간 순서)__

    ```
    1 > 2 > 7 > 6 > 8 > 3 > 4 > 5
    ```

### DFS Python 소스 코드 예시

```python
"""
# DFS 메소드 정의
graph : 2차원 리스트 형태의 그래프
node : 방문할 노드 번호
visited : 각 노드의 방문 여부를 담은 1차원 리스트
"""
def dfs(graph, node, visited):
    # 현재 노드를 방문 처리
    # 첫 방문 노드는 초기화에서 False 였기 때문에 True로 바로 변경
    visited[node] = True

    print(node, end=" ")

    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for next_node in graph[node]:
        # 해당 노드와 연결된 인접 노드가 방문했는지 판단하고,
        # 방문하지 않았으면 해당 노드를 방문 처리
        if not visited[next_node]:
            dfs(graph, next_node, visited)

# 각 노드가 연결된 정보를 표현(2차원 리스트 객체)
# 2차원 배열 형태로 노드 간 연결된 정보를 표시
# 첫 번째 리스트의 인덱스는 각 노드의 번호
# 각 노드 안에 있는 리스트는 해당 인덱스와 연결된 노드 번호
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

# 각 노드가 방문된 정보를 표현(1차원 리스트 객체)
# index 0번을 포함하여 8개의 노드가 존재하기 때문에 List의 길이는 9
visited = [False] * 9

# 정의된 DFS 메소드 호출
# Index 번호가 가장 낮은 노드부터 호출
dfs(graph, 1, visited) # 1 2 7 6 8 3 4 5
```

---

## BFS (Breadth-First Search)

BFS는 __너비 우선 탐색__ 이라고 부르며, 그래프에서 __가까운 노드부터 우선적으로 탐색__ 하는 알고리즘

BFS는 __큐 자료구조__ 를 이용

__특정 조건에서 최단 경로를 찾는 문제__ 에서 자주 사용

__각 간선의 비용이 모두 동일__ 한 상황에서 __최단 거리 문제를 해결__ 하기 위한 목적으로도 사용

- BFS의 동작 과정

    1. 탐색 시작 노드를 큐에 삽입하고 방문 처리
    2. 큐에서 노드를 꺼낸 뒤 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문 처리
    3. 더 이상 2 번의 과정을 수행할 수 없을 때까지 반복

예시)

(DFS의 그래프와 동일한 무방향 그래프)

![Alt Text][03_dfs_graph_01]

__[Step 0]__ 그래프를 준비 : 시작 노드 1

- 방문 기준 : 번호가 낮은 인접 노드부터 방문

__[Step 1]__ 시작 노드인 '1'을 큐에 넣고 방문 처리 : `[1]`

__[Step 2]__ 큐에서 노드 '1'을 꺼내 방문하지 않은 인접 노드 '2, 3, 8'을 큐에 넣고 방문 처리 : `[2, 3, 8]`

__[Step 3]__ 큐에서 노드 '2'를 꺼내 방문하지 않은 인접 노드 '7'을 큐에 넣고 방문 처리 (1은 이미 방문 처리 되어 있기 때문에 방문하지 않음) : `[3, 8, 7]`

__[Step 4]__ 큐에서 노드 '3'을 꺼내 방문하지 않은 인접 노드 '4, 5'를 큐에 넣고 방문 처리 : `[8, 7, 4, 5]`

__[Step 5]__ 큐에서 노드 '8'을 꺼내지만, 방문하지 않은 인접 노드가 없기 때문에 무시 : `[7, 4, 5]`

- 해당 과정을 반복하였을 때 __전체 노드의 탐색 순서(큐에 들어간 순서)__

    ```
    1 > 2 > 3 > 8 > 7 > 4 > 5 > 6
    ```



### BFS Python 소스 코드 예시

```python
# Queue 자료 구조를 사용하기 위한 Deque 라이브러리 사용
from collections import deque

# BFS 메소드 정의 (파라미터는 DFS와 동일)
def bfs(graph, node, visited):
    # Queue에 방문한 Node를 넣음
    queue = deque([node])

    # 현재 노드 방문 처리
    visited[node] = True

    # 큐가 빌 때까지 반복 : DFS와 달리 재귀함수를 사용하지 않음
    while queue:
        # 큐에서 가장 먼저 들어온 원소 추출
        last_node = queue.popleft()

        print(last_node, end=" ") # 출력

        # 해당 노드와 연결된 노드를 탐색
        for near_node in graph[last_node]:
            # 연결된 노드가 방문 처리가 안되어있다면,
            if not visited[near_node]:
                # Queue에 해당 노드를 넣고,
                queue.append(near_node)
                # 노드를 방문 처리
                visited[near_node] = True

# 각 노드가 연결된 정보를 표현한 2차원 리스트 객체 (DFS와 동일)
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

# 각 노드가 방문된 정보를 1차원 리스트를 기반으로 표현 (DFS와 동일)
visited = [False] * 9

# BFS 메소드 호출
bfs(graph, 1, visited) # 1 2 3 8 7 4 5 6
```

## DFS & BFS 문제 풀이

### 예시 1) 음료수 얼려 먹기 (Connected Component 찾기 문제)

N * M 크기의 얼음 틀이 있는데, 구멍이 뚫려 있는 부분은 0, 칸막이가 존재하는 부분은 1

구멍이 뚫려 있는 부분끼리 상,하,좌,우로 붙어 있는 경우 서로 연결되어 있는 것으로 간주

얼음 틀의 모양이 주어졌을 때 생성되는 총 아이스크림의 개수 구하기

예시)

4 * 5 의 얼음 틀에서 아래와 같은 연결 정보에서 아이스크림 생성 수 : 3개

```
00110
00011
11111
00000
```

- 첫 번째 줄에 얼음 틀의 세로 길이 N과 가로 길이 M
- 두 번째 줄부터 N + 1 번째 줄까지 얼음 틀의 형태가 주어짐
- 구멍이 뚤린 부분은 0, 그렇지 않은 부분은 1

- 문제 풀이

    - 문제 해결 아이디어

        __DFS | BFS__ 로 서로 연결되어 있는 연결 요소가 몇 개 있는지 해결 가능

        상하좌우로 연결된 얼음틀들은 인접한 노드들로 표현 가능

    - DFS 기반의 문제 풀이 알고리즘

        1. 특정 지점의 주변 상,하,좌,우를 살펴본 뒤에 주변 지점 중에서 값이 '0'이면서 아직 방문하지 않은 지점이 있따면 해당 지점을 방문
        2. 방문한 지점에서 다시 상,하,좌,우를 살펴보면서 방문을 진행하는 과정을 반복하면, 연결된 모든 지점을 방문 가능
        3. 모든 노드에 대해서 1, 2번의 과정을 반복하며, 방문하지 않은 지점의 수를 카운트

```python
# DFS로 특정 노드를 방문하고 연결된 모드 노드들도 방문
def dfs(x, y):
    # 얼음틀을 벗어나는 범위일 경우 False 반환
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False

    # 현재 노드를 아직 방문하지 않았다면
    # 초기에 graph[x][y]의 값이 1일 경우 이미 방문 처리 하는 이유는 막혀있다는 것을 표시하기 위함
    # 0일 경우에는 방문을 하지 않았다고 표시하고 연결되어있을 경우 1로 바꾸면서 방문 처리
    # 상, 하, 좌, 우 재귀적으로 호출하면서 사방이 1로 막힌 경우를 지속적으로 찾음
    if graph[x][y] == 0:
        # 해당 노드 방문 처리 : 연결되어있음 처리
        graph[x][y] = 1
        # 상, 하, 좌, 우의 위치들도 모두 재귀적으로 호출
        # 재귀적으로 호출하면서 연결되어있음을 인지
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)

        # 초기 graph[x][y] 값이 0이 었기 때문에 해당 원소만 뚫려있을 경우에도 True로 반환되어 count가 올라감
        return True

    # graph[x][y]가 1일 경우에는 막혀있기 때문에 False
    return False

# N, M을 공백을 기준으로 입력
n, m = map(int, input().split())

# 2차원 리스트의 맵 정보 입력 받기
graph = []
for i in range(n):
    # 한 줄 안에서 구분자 없이 각 원소의 입력 값을 받기 때문에 int 형변환 후 Mapping
    graph.append(list(map(int, input())))

# 모든 노드(위치)에 대하여 음료수 채우기
result = 0

for i in range(n):
    for j in range(m):
        # 각 위치에서 DFS 수행
        if dfs(i, j) == True:
            result += 1

print(result) # 정답 출력
```

### 예시 2) 미로 탈출

N * M 크기의 직사각형 형태의 미로에 여러 마리의 괴물을 피해 탈출

주인공의 위치는 (1, 1)이며, 미로의 출구는 (N, M)의 위치에 존재하며 한 번에 한 칸씩 이동 가능

이 떄 괴물이 있는 부분은 0, 괴물이 없는 부분은 1로 주어지는데,

탈출하기 위해 움직여야 하는 최소 칸의 개수를 구하기 (시작, 마지막 칸을 모두 포함해서 계산)

- 첫 째 줄 : 두 정수 N, M(4 <= N, M <= 200)이 주어지고, 다음 N개의 줄에는 각각 M개의 정수 (0 | 1)이 주어짐

- 각각의 수들은 공백 없이 붙어서 제시

- 시작 칸과 마지막 칸은 항상 1

예시)

```
5 6
101010
111111
000001
111111
111111
```

```
10
```

- 문제 풀이

    - 문제 해결 아이디어

        BFS는 시작 지점에서 가까운 노드부터 차례대로 그래프의 모든 노드를 탐색

        상, 하, 좌, 우로 연결된 __모든 노드로의 거리가 동일__

        따라서, (1, 1) 지점부터 BFS를 수행하여 모든 노드의 최단 거리 값을 기록하면 해결 가능

        예시)

        ```text
        110             (1) - (1) - (0)
        010       =>    (0) - (1) - (0)
        011             (0) - (1) - (1)
        ```

        __[Step 1] (1, 1)에서 BFS 수행__

        인접 노드 중에서 1인 노드만 방문 가능하다고 정의하여 Queue에 노드를 넣고 방문 처리 할 때 노드의 초기 값이 1인 경우에 한해서만 BFS 수행

        __[Step 2] (1, 1) 좌표에서 상, 하, 좌, 우로 탐색을 진행__

        바로 옆 노드인 (1, 2) 위치의 노드를 방문하게 되고, 새롭게 방문하는 (1, 2) 노드의 값을 2로 바꿈

        2로 바꾸는 이유는 시작 위치부터 마지막 위치까지 도달하는 최단 경로에 포함되어 있는 노드의 수를 출력해야 하기 때문

        마찬가지로 인접한 노드 방문하여 방문 처리 할 때 노드의 초기 값이 1인 경우에 한해서만 BFS 수행

        __[Step 3] BFS를 계속 수행하면, 결과적으로 최단 경로의 값들이 1씩 증가하는 형태로 나옴__

        마지막 노드의 값을 출력시키면 최단 거리가 나옴

```python
from collections import deque

# BFS를 통한 최단 거리 측정
# 미로의 좌표 값을 받음
def bfs(x, y):
    # Queue 구현을 위해 Deque 라이브러리 사용
    queue = deque()

    # 해당 좌표값을 Queue에 추가
    queue.append((x, y))

    # Queue가 빌 때까지 반복
    while queue:
        # Queue 원소 추출
        x, y = queue.popleft()

        # 현재 위치에서 인접(상, 하, 좌, 우) 좌표 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 미로 찾기 공간을 벗어난 경우
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            # 괴물이 있는 경우
            if graph[nx][ny] == 0:
                continue

            # 해당 노드를 처음 방문하는 경우에만 최단 거리에 기록
            # 처음 방문하는 경우가 아니라면 1을 초과하는 값이 들어있으므로 중복 방문 처리를 수행할 수 있음
            # 1인 경우 해당 좌표가 괴물이 없고 방문 처리를 하지 않았다는 의미
            if graph[nx][ny] == 1:
                # 이전 좌표의 원소 값(최단 경로 값) + 1
                graph[nx][ny] = graph[x][y] + 1

                # Queue에 추가
                queue.append((nx, ny))

    # 가장 오른쪽 아래까지의 최단 거리 반환
    return graph[n - 1][m - 1]

n, m = map(int, input().split()) # N, M 입력 받기

# 2차원 리스트 형태의 맵 정보 입력
graph = []

for i in range(n):
    graph.append(list(map(int, input())))

# 이동할 네 가지 방향 정의 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 시작 지점(0, 0)에서부터 BFS 탐색 수행
print(bfs(0, 0))
```

---

## Reference.

- [동빈나 Youtube : 이코테 2021 3장](https://youtu.be/m-9pAwq1o3w?feature=shared)

[03_dfs_graph_01]:https://imgur.com/bBNdvP0.png