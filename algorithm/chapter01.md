[< 목차 바로 가기](../README.md)

[Chapter 02. 이동 >](./chapter02.md)

# 동빈나 알고리즘 강의 Chapter 01.

> 코딩 테스트 출제 경향 분석 및 파이썬 문법 부수기

# 코딩 테스트

기업/기관에서 연수생을 선발하기 위한 문제 풀이 시험 (주로 공개 채용하는 기업에서 진행)

### 코딩 테스트 시행 이유

1. 문제 해결 역량 평가
2. 채점 시스템을 통해 응시자 수 효과적인 감소

## 코딩 테스트 유형

### 1. 온라인 코딩 테스트 (주)

인터넷을 통해 프로그래밍 역량 평가, 대체로 타인과 문제풀이를 공유하지 않는 선에서 인터넷 검색 허용하는 경우가 있음

### 2. 오프라인 코딩 테스트

시험장에 방문하여 시험 수행, 인터넷 검색이 허용되지 않으며, 회사에서 제공하는 컴퓨터 환경을 이용해 진행

### Online Judge

코딩 테스트 및 프로그래밍 대회에 나올 법한 문제를 시험해보는 시스템

- 해외

1. 코드포스(Codeforces) : www.codeforces.com
2. 탑코더(TopCoder) : www.topcoder.com
3. 릿코드(LeetCode) : leetcode.com
4. 코드셰프(CODECHEF) : www.codechef.com

- 국내

1. 백준 온라인 저지(BOJ) : www.acmicpc.net - 다수의 대기업 기출문제가 존재하며, 유형별로 풀기 가능, 국내 사용자들이 다수 존재 (추천)
2. 코드업(CodeUp) : codeup.kr - 처음 코딩테스트를 접할 때 좋음
3. 프로그래머스(Programmers) : programmers.co.kr - 인기 IT 대기업 문제 및 다양한 문제 포함 (추천)
4. SW Expert Academy : swexpertacademy.com

## 코딩 테스트 환경

### 1. (추천) 리플릿

- Link : https://repl.it/languages/python3

### 2. (초보용) 파이썬 튜터

- Link : http://pythontutor.com/visualize.html

## 소스 코드 관리

알고리즘 코딩 테스트 준비 과정에서 자신만의 소스 코드를 관리하는 것이 좋음 (라이브러리화)

## IT 기업 코딩 테스트 경향

대부분의 대기업은 알고리즘 코딩 테스트 시행

2~5시간 가량의 시간 동안 여러 개의 알고리즘 문제를 풀이함

### 가장 출제 빈도가 높은 유형

1. 그리디 알고리즘
2. 구현
3. DFS/BFS 기반 탐색

- 카카오의 경우 문제 풀이를 안내

---

# 알고리즘 성능 평가

__복잡도(Complexity)__ 는 알고리즘의 성능을 나타내는 척도

- 시간 복잡도 : 특정한 크기의 입력에 대하여 알고리즘의 수행 시간 분석
- 공간 복잡도 : 특정한 크기의 입력에 대해서 알고리즘의 메모리 사용량 분석

동일한 기능을 수행하는 알고리즘이 있다면, 일반적으로 _복잡도가 낮을수록 좋은 알고리즘_

## 빅오 표기법(Big-O Notation)

__가장 빠르게 증가하는 항__ 만을 고려하는 표기법으로, 함수의 상한만을 나타내게 된다.

예) 연산 횟수가 3N^3 + 5N^2 + 1,000,000인 알고리즘이 있을 때, 빅오 표기법에서는 차수가 가장 큰 항만을 남기므로 __O(N^3)__ 이 된다.

### 빅오 표기법 순위표

순위가 높을수록 좋음

|No.|순위|명칭|
|:---:|:---:|---|
|1|O(1)|상수 시간(Constant Time)|
|2|O(logN)|로그 시간(Log Time)|
|3|O(N)|선형 시간|
|4|O(NlogN)|로그 선형 시간|
|5|O(N^2)|이차 시간|
|6|O(N^3)|삼차 시간|
|7|O(2^n)|지수 시간|

예시 1)

N개의 데이터의 합을 계산하는 프로그램 예제

```python
array = [3,5,1,2,4] # 5개의 데이터 (N=5)
summary = 0 # 합계를 저장할 변수

# 모든 데이터를 하나씩 확인하며 합계를 계산
for x in array:
    summary += x

# 결과 출력
print(summary)
```

-> 수행 시간은 array의 길이(N)에 비례할 것임을 예측할 수 있다. 따라서 시간 복잡도는 __O(N)__ 이 된다.

예시 2)

2중 반복문을 사용하는 프로그램 예제

```python
array = [3,5,1,2,4] # 5개의 데이터 (N=5)

for i in array:
    for j in array:
        temp = i * j
        print(temp)
```

반복문과 그 안의 반복문 모두 array의 길이(N)에 따라 처리량이 달라지기 때문에 시간 복잡도는 __O(N^2)__ 가 된다.

다만, 모든 이중 반복문이 동일한 시간 복잡도를 갖지는 않는다.

## 알고리즘 설계 Tip

1. 일반적으로 CPU 기반 개인 컴퓨터 | 채점용 컴퓨터에서 연산 횟수가 _5억_ 을 넘어가는 경우
    - __C언어__ 기준 통상 __1~3초__ 소요
    - __Python__ 기준 통상 __5~15초__ 소요 _(단, PyPy의 경우 간혹 C언어보다 빠른 경우 존재)_
2. _O(N^3)_ 의 알고리즘의 경우 N의 값이 _5,000_ 을 넘어간다면?
3. 코딩 테스트 문제에서 시간 제한은 통상 __1~5초__ (명시되어 있지 않은 경우 5초 정도가 마지노선)

### 요구사항에 따라 적절한 알고리즘 설계

문제에서 가장 먼저 확인해야할 사항은 __시간 제한(수행시간 요구사항)__ 으로, 시간에 따라 적절하게 알고리즘을 선택하는 것이 중요

예) 시간 제한이 1초인 문제일 때 일반적인 기준

- N의 범위 500 : 시간 복잡도가 O(N^3)인 알고리즘 설계
- N의 범위 2,000 : 시간 복잡도가 O(N^2)인 알고리즘 설계
- N의 범위 100,000 : 시간 복잡도가 O(NlogN)인 알고리즘 설계
- N의 범위 10,000,000 : 시간 복잡도가 O(N)인 알고리즘 설계

### 알고리즘 문제 해결 과정

1. 지문 분석 및 컴퓨터적 사고를 통한 문제 분해
2. 요구사항(복잡도) 분석
3. 문제 해결을 위한 아이디어 도출
4. 소스 코드 설계 및 코딩

일반적으로 핵심 아이디어를 도출하면, 간결하게 소스 코드를 작성할 수 있는 형태로 출제

- 수행 시간 측정 소스 코드 예시 (Python)

    ```python
    import time
    start_time = time.time() # 측정 시작

    """
    프로그램 소스 코드
    """

    end_time = time.time()

    print("Time : ", end_time - start_time) # 수행 시간 출력
    ```

---

# 자료형

Python에서는 **[정수형, 실수형, 복소수형, 문자열, 리스트, 튜플, 사전(딕셔너리)]** 이 존재함.

### 정수형 (Integer)

정수를 다루는 자료형으로, **양의 정수, 음의 정수, 0** 이 포함되며, 코딩 테스트에서 출제되는 많은 문제들은 정수형을 주로 다루게 된다.

### 실수형 (Real Number)

**소수점 아래의 데이터를 포함하는 수 자료형** 으로, Python에서는 변수에 소수점을 붙인 수를 대입하면 실수형 변수로 처리된다.

소수부가 0이거나, 정수부가 0인 소수는 생략하고 작성 가능.

```python
a = 157.93
print(a) # 157.93

a = 5.
print(a) # 5.0

a = -.7
print(a) # -0.7
```

IEEE754 표준에서는 **실수형을 저장하기 위해 4byte | 8byte의 고정된 크기의 메모리를 할당** 하므로, 컴퓨터 시스템은 실수 정보를 표현하는 정확도에 한계를 가짐.

예를 들어 10진수 체계에서는 0.3 + 0.6이 정확하게 0.9로 나오지만, 2진수에서는 0.9를 정확하게 표현할 수 있는 방법이 없기 때문에 *최대한 0.9와 가깝게 표현하고 실제로는 미세한 오차를 발생* 시킴.

이를 해결하기 위해 __round()__ 메소드를 사용하며, 이것이 권장되는 방법

예를들어 123.456을 소수 셋째 자리에서 반올림하면 `round(123.456, 2)` 라고 작성하면 123.46이 나옴.

```python
# 기본적인 실수형 표현
a = 0.3 + 0.6
print(a) # 0.899999999...

# False
if a == 0.9:
    print(True)
else:
    print(False)

# round()를 활용한 실수형 표현
a = 0.3 + 0.6 # 0.899999...
print(round(a, 4)) # 소수점 넷째자리에서 반올림하기 때문에 0.9가 출력

# True
if round(a, 4) == 0.9:
    print(True)
else:
    print(False)
```

### 지수 표현 방식

Python에서는 __e__ 혹은 __E__ 를 이용한 지수 표현 방식을 이용할 수 있는데, e(E) 다음에 오는 수는 10의 지수부를 의미 (실수형 데이터로 표현)

ex) 1e9 = 10의 9제곱 (1,000,000,000)

지수 표현 방식은 임의의 큰 수를 표현하기 위해 자주 사용되며, 최단 경로 알고리즘에서는 도달할 수 없는 노드에 대해서 최단 거리를 무한(INF)으로 설정하는 경우도 있는데, 이 떄 가능한 최댓값이 10억 미만이라면, 무한(INF)의 값으로 1e9를 이용할 수 있음.

```python
a = 1e9
print(a) # 1000000000.0

a = 75.25e1
print(a) # 752.5

a = 3954e-3
print(a) # 3.954
```

만약 실수형 데이터를 정수로 변환해야하는 경우에는 int()로 파싱

### 수 자료형의 연산

수 자료형은 사칙연산과 나머지 연산자가 많이 사용되는데, 기본적으로 나누기 연산자는 정수형(몫)으로 나오지만, Python에서는 나누기 연산자(/)의 결과를 실수형으로 반환

따라서, 다양한 로직을 설계할 때 나머지 연산자(%)를 이용해야 할 때가 많음. (예: a가 홀수인지 확인하는 경우)

Python에서는 몫을 얻기 위해 몫 연산자(//)를 사용하고, 이 외에도 거듭 제곱 연산자(**)를 비롯해 다양한 연산자들이 존재

```python
a = 7
b = 3

# 나누기
print(a / b) # 2.3333333333.5

# 나머지
print(a % b) # 1

# 몫
print(a // b) # 2

a = 5
b = 3

# 거듭 제곱
print(a ** b) # 125

# 제곱근
print(a ** 0.5) # 2.23606797749979
```

---

# 리스트 자료형

리스트 자료형은 _여러 개의 데이터를 연속적으로 담아 처리하기 위해 사용하는 자료형_ 으로, C | Java의 __배열(Array)__ 및 __연결 리스트(Linked List)__ 와 유사한 기능 지원

C++의 __STL Vector__ 과 기능적으로 유사하며, 리스트 대신 배열 혹은 테이블이라고도 부름.

리스트 초기화는 대괄호 안에 원소를 넣어 초기화하며, 쉼표로 원소를 구분. 비어 있는 리스트를 선언하고자 할 때는 list() 혹은 `[]` 를 사용

리스트의 원소에 접근할 때는 인덱스(Index) 값을 괄호에 넣음 **(Index는 0부터 시작)**

```python
a = [1,2,3,4,5,6,7,8,9] # 직업 데이터를 넣어서 초기화

print(a) # [1,2,3,4,5,6,7,8,9]

print(a[3]) # 네 번째 원소만 출력 (0부터 시작) : 4

# 크기가 N이고, 모든 값이 0인 1차원 리스트 초기화
n = 10
a = [0] * n # 리스트의 길이만큼 곱셈

print(a) # [0,0,0,0,0,0,0,0,0,0]
```
### 리스트의 인덱싱과 슬라이싱

인덱스 값을 입력하여 리스트의 특정 원소에 접근하는 것을 __인덱싱(Indexing)__ 이라고 하는데, 파이썬의 인덱스 값은 __양|음의 정수__ 모두 사용 가능한데, 음의 정수를 넣으면 원소를 거꾸로 탐색

```python
a = [1,2,3,4,5,6,7,8,9]

print(a[7]) # 8번째 원소 출력 : 8

print(a[-1]) # 뒤에서 1번째 원소 출력 : 9

print(a[-3]) # 뒤에서 3번째 원소 출력 : 7

a[3] = 7 # 네 번째 원소 7로 변경

print(a) # [1,2,3,7,5,6,7,8,9]
```

리스트에서 연속적인 위치를 갖는 원소들을 가져와야 할 때는 __슬라이싱(Slicing)__ 을 사용하는데, 대괄호 안에 __콜론(:)__ 을 넣어 시작 인덱스와 끝 인덱스를 설정하고, _끝 인덱스는 실제 인덱스보다 1을 더 크게 설정_

```python
a = [1,2,3,4,5,6,7,8,9]

print(a[1:4]) # 2번쨰 원소부터 4번쨰 원소까지 : [2,3,4]
```

### 리스트 컴프리헨션

리스트를 초기화하는 방법 중 하나로, 대괄호 안에 조건문과 반복문을 적용하여 리스트를 초기화 할 수 있음

긴 코드를 간결화 할 수 있다는 것이 좋음

```python
# 0부터 9까지의 수를 포함하는 리스트
array = [i for i in range(10)]

print(array) # [0,1,2,3,4,5,6,7,8,9]

# 조건문 포함
array = [i for i in range(20) if i % 2 == 1] # 0~19 중에서 홀수만 포함하는 리스트

print(array) # [1,3,5,7,9,11,15,17,19]
```

리스트 컴프리헨션은 __2차원 리스트를 초기화__ 할 때 유용하게 사용하는데, 특히 N * M 크기의 2차원 리스트를 한 번에 초기화 할 때 사용

예) `array = [[0] * m for _ in range(n)]`

만약 2차원 리스트를 초기화 할 때 다음과 같이 작성하면 예기치 않은 결과가 나올 수 있음

잘못된 예) `array = [[0] * m] * n` : 해당 코드는 전체 리스트 안에 포함된 각 리스트가 모두 같은 객체로 인식되는 문제가 발생

```python
n = 4
m = 3

array = [[0] * m for _ in range(n)]

print(array) # [[0,0,0], [0,0,0], [0,0,0]]

# 잘못된 방법
n = 4
m = 3

array = [[0] * m] * n

print(array)

array[1][1] = 5 # 모두 같은 객체로 인식되어 값이 잘못 변경됨 [[0,5,0], [0,5,0], [0,5,0]]
```

Python에서는 반복을 수행하되 __반복을 위한 변수의 값을 무시하고자 할 때__ 언더바(_)를 사용

```python
# 1부터 9까지의 자연수 더하기
summary = 0

for i in range(1,10):
    summary += i

print(i)

# "Hello World"를 5번 출력 : 반복을 위한 변수의 값 무시
for _ in range(5):
    print("Hello World")
```

### 리스트 관련 메소드

|함수명|사용법|설명|시간 복잡도|
|---|---|---|:---:|
|append()|변수명.append()|리스트에 원소 하나를 사입할 때 사용|O(1)|
|sort()|변수명.sort(reverse=True)|기본 정렬 기능으로, 파라미터가 없으면, 오름차순 정렬이며, __reverse__ 파라미터가 __True__ 값이면 내림차순 정렬|O(NlogN)|
|reverse()|변수명.reverse()|리스트의 원소 순서를 뒤집어 놓음|O(N)|
|insert()|변수명.insert(index, value)|index 위치에 value 원소를 삽입|O(N)|
|count()|변수명.count(value)|리스트에서 value 값을 가지는 데이터 개수를 셀 때 사용|O(N)|
|remove()|변수명.remove(value)|value 값을 갖는 원소를 제거하는데, __여러 개라면 하나만 제거__|O(N)|

리스트에서 특정 값을 가지는 원소를 모두 제거하는 방법

```python
a = [1,2,3,4,5,5,5]

remove_set = {3, 5} # 집합 자료형

result = [i for i in a if i not in remove_set] # remove_set 안에 포함되어 있는 변수를 제외한 나머지 변수를 result 리스트에 넣음

print(result)
```

---

# 문자열 자료형

문자열 변수를 초기화할 때는 큰따옴표 | 작은따옴표 사용하는데, 만약 문자열 안에 해당 문자가 포함되어야 하는 경우 백슬래시(\)를 사용하면 포함시킬 수 있음

### 문자열 연산

__덧셈(+), 곱셈(*)__ 을 사용하게 되면 문자열이 더해지거나 곱셈한 수만큼 문자열이 추가

리스트와 마찬가지로 __인덱싱__ 과 __슬라이싱__ 을 사용할 수는 있지만, 인덱스의 값을 변경할 수는 없음.

---

# 튜플 자료형

리스트와 유사하지만 문법적 차이가 발생

- 한 번 선언된 값을 _변경할 수 없음_
- 리스트는 대괄호를 사용하지만, 튜플은 __소괄호(())__ 를 사용

튜플은 리스트에 비해 상대적으로 공간 효율성이 높음

```python
a = (1,2,3,4,5,6,7,8,9)

print(a[3]) # 4번째 원소만 출력 : 4

print(a[1:4]) # 2번째 원소부터 4번째 원소까지 출력 (2,3,4)

# 오류
a[2] = 7 # 불가능
```

### 튜플을 사용하면 좋은 경우

1. 서로 다른 성질의 데이터를 묶어서 관리하는 경우 (예: 최단 경로 알고리즘에서 비용, 노드 번호의 형태로 튜플 자료형 사용)
2. 데이터의 나열을 __해싱(Hashing)__ 의 키 값으로 사용할 때 튜플의 변경 불가 속성을 이용하여 키 값으로 사용 가능
3. 리스트보다 __메모리 효율성__ 을 높여야 할 때

---

# 사전 자료형

사전 자료형은 __키(Key)__ 와 __값(Value)__ 의 쌍을 데이터로 갖는 자료형으로, 리스트와 튜플이 값을 순차적으로 저장하는 것과는 대비

사전 자료형은 키와 값의 쌍을 데이터로 가지며, 원하는 __변경 불가능(Immutable) 자료형__ 을 키로 사용할 수 있음.

Python의 사전 자료형은 _해시 테이블(Hash Table)_ 을 이용하므로, 데이터의 조회 및 수정에 있어서 __O(1)__ 의 시간에 처리 가능

```python
data = dict()

data["사과"] = "Apple"
data["바나나"] = "Banana"
data["코코넛"] = "Coconut"

print(data) # {"사과": "Apple", "바나나": "Banana", "코코넛": "Coconut"}

# 특정 키가 존재하는지 검사가 가능 (O(1))
if "사과" in data:
    print("'사과'를 키로 가지는 데이터가 존재합니다.")
```

사전 자료형에서는 키와 값을 별도로 뽑아내기 위한 메소드가 존재

- 키 데이터만 추출하여 리스트로 만들 때는 `변수명.keys()` 함수를 사용
- 값 데이터만 추출하여 리스트로 만들 때는 `변수명.values()` 함수를 사용

```python
data = dict()

data["사과"] = "Apple"
data["바나나"] = "Banana"
data["코코넛"] = "Coconut"

key_list = data.keys() # Key List 추출
value_list = data.values() # Value List 추출

print(key_list) # dict_keys(["사과", "바나나", "코코넛"])
print(value_list) # dict_values(["Apple", "Banana", "Coconut"])

# 사전 자료형에서 key, value 목록을 뽑아낸 후 List 객체로 만들고 싶은 경우 list() 메소드를 사용
key_list = list(key_list)
value_list = list(value_list)

# 각 키에 따른 값을 하나씩 출력하고 싶은 경우
# Apple / Banana / Coconut
for key in key_list:
    print(data[key])
```

---

# 집합 자료형

집합 특징

1. 중복을 허용하지 않음
2. 순서가 없음

위의 특징으로 인해 어떤 데이터가 존재하는지 체크할 때 편리함

집합은 리스트 | 문자열을 이용해서 초기화 하는데, `set()` 함수를 사용하거나, __중괄호 ({})__ 안에 각 원소를 __콤마(,)__ 를 기준으로 구분하여 삽입함으로써 초기화 가능

데이터의 조회 및 수정에 있어서 __O(1)__ 의 시간에 처리할 수 있음

```python
data = set([1,1,2,3,4,4,5]) # 초기화 방법 1 : 중복되는 원소는 제거

data = {1,1,2,3,4,4,5} # 초기화 방법 2

print(data) # 위의 두개 모두 {1,2,3,4,5} 로 같은 결과를 보여줌
```

### 집합 자료형의 연산

- 합집합 : 집합 A에 속하거나 B에 속하는 원소로 이루어진 집합
- 교집합 : 집합 A에도 속하고 B에도 속하는 원소로 이루어진 집합
- 차집합 : 집합 A의 원소 중에서 B에 속하지 않는 원소들로 이루어진 집합

```python
a = set([1,2,3,4,5])
b = set([3,4,5,6,7])

# 합집합
print(a | b) # {1,2,3,4,5,6,7}

# 교집합
print(a & b) # {3,4,5}

# 차집합
print(a - b) # {1,2}
```

### 집합 자료형 관련 함수

```python
data = set([1,2,3])

# 원소 추가
data.add(4)
print(data) # {1,2,3,4}

# 원소 여러 개 추가
data.update([5,6])
print(data) # {1,2,3,4,5,6}

# 특정한 값을 갖는 원소 삭제
data.remove(3)
print(data) # {1,2,4,5,6}
```

### 사전 & 집합 자료형 특징

- 리스트 | 튜플은 순서가 있기 때문에 인덱싱을 통해 자료형의 값을 얻을 수 있음
- 사전 | 집합 자료형은 순서가 없기 때문에 인덱싱으로 값을 얻을 수 없음
    - __사전 : 키, 집합 : 원소__ 를 이용해 __O(1)__ 의 시간 복잡도로 조회 가능

---

# 기본 입출력

모든 프로그램은 적절한 입출력 양식을 갖고 있는데, 프로그램 동작의 첫 번째 단계는 데이터를 입력 받거나 생성하는 것 (예: 학생의 성적 데이터가 주어지고, 이를 내림차순으로 정렬하는 프로그램 등)

### 자주 사용되는 표준 입력 방법

- `input()` : 한 줄의 문자열을 입력 받음
- `map()` : 리스트의 모든 원소에 각각 특정한 함수를 적용

__예시 1)__ 공백을 기준으로 구분된 데이터를 입력 받는 경우

`list(map(int, input().split()))` : 공백을 기준으로 문자열을 분리하고, integer 형변환 후, List 객체로 선언 (많이 사용되기 때문에 손에 익을 때까지 사용하는 것을 추천)

__예시 2)__ 공백을 기준으로 구분된 데이터의 개수가 많지 않다면, 다음과 같이 사용

`a, b, c = map(int, input().split())`

```python
n = int(input()) # 데이터의 개수 입력

# 각 데이터를 공백을 기준으로 구분하여 입력
data = list(map(int, input().split()))

# 정렬 후 출력
data.sort(reverse=True)

print(data) # [높은 순서대로 내림차순]
```

### 입력을 위한 전형적인 코드

```python
n, m, k = map(int, input().split())

print(n, m, k)
```

### 빠르게 입력 받기

사용자로부터 입력을 _최대한 빠르게 받아야 하는 경우_ : Python의 경우 __sys__ 라이브러리에 정의되어 있는 `sys.stdin.readline()` 메소드를 사용

단, 입력 후 __엔터(Enter)__ 가 줄 바꿈 기호로 입력되기 때문에 `rstrip()` (줄바꿈 입력 제거) 메소드를 함께 사용

실제로 이진탐색, 정렬 등에서 많이 사용

```python
import sys

data = sys.stdin.realine().rstrip()

print(data)
```

### 자주 사용되는 표준 출력 방법

Python에서 기본 출력은 `print()` 를 사용하는데, 각 변수를 __콤마(,)__ 를 사용하여 띄어쓰기로 구분하여 출력

print()는 기본적으로 __출력 이후 줄 바꿈 수행__ (원치 않는 경우 `end` 속성 사용)

```python
a = 1
b = 2
print(a, b) # 기본적으로 띄어쓰기로 변수 구분
print(7, end=" ") # 엔터 대신 띄어쓰기
print(8, end=" ")

# 출력할 변수
answer = 7
print("정답은 " + str(answer) + "입니다.")
```

### f-string 예제

Python에서 문자열 앞에 접두사 __f__ 를 붙여 사용

중괄호 안에 변수명을 기입하여 간단히 문자열과 정수를 함께 넣을 수 있음

```python
answer = 7
print(f"정답은 {answer}입니다.")
```

---

# 조건문

__프로그램의 흐름을 제어__ 하는 문법으로 이를 이용해 조건에 따라 프로그램의 로직을 설정 가능

```python
x = 15

if x >= 10:
    print("x >= 10")

if x >= 0:
    print("x >= 0")

if x >= 30:
    print("x >= 30")
```

조건문의 기본 형태 : `if ~ elif ~ else` (elif, else는 옵션)

### 비교 연산자

대입 연산자 (=)와 같음 연산자(==)는 다름

|비교 연산자|설명|
|:---:|---|
|X == Y|X와 Y가 서로 같을 때 참(True)|
|X != Y|X와 Y가 서로 다를 때 참(True)|
|X > Y|X가 Y보다 클 때 참(True)|
|X < Y|X가 Y보다 작을 때 참(True)|
|X >= Y|X가 Y보다 크거나 같을 때 참(True)|
|X <= Y|X가 Y보다 작거나 같을 때 참(True)|

### 논리 연산자

__논리 값(True/False)__ 사이의 연산을 수행할 때 사용

|논리 연산자|설명|
|:---:|---|
|X and Y|X와 Y가 모두 참(True)일 때 참(True)|
|X or Y|X와 Y 중에 하나만 참(True)일 때 참(True)|
|not X|X가 거짓(False)일 때 참(True)|

### 기타 연산자

다수의 데이터를 담는 자료형을 위해 __in 연산자__ 와 __not in 연산자__ 가 제공 (리스트, 튜플, 문자열, 딕셔너리 모두 사용 가능)

|기타 연산자|설명|
|:---:|---|
|x in 리스트|리스트 안에 x가 들어있을 때 참(True)|
|x not in 리스트|문자열 안에 x가 들어있지 않을 때 참(True)|

### Pass 키워드

Python에서 아무것도 처리하고 싶지 않을 때 __pass__ 키워드 사용

예시) 디버깅 과정에서 조건문의 형태만 만들어 놓고 처리하는 부분을 비워놓고 싶은 경우 사용

### 조건문 간소화

실행될 코드가 한 줄일 경우, 굳이 줄 바꿈을 하지 않고 표현 가능

예시) `if score >= 80: result = "Success`

- 조건부 표현식(Conditional Expression) : if ~ else 문을 한 줄에 작성 가능

예시) `result = "Success if score >= 80 else "Fail"`

### 들여쓰기

Python 에서는 __코드의 블록(Block)__ 을 `들여쓰기(Indent)` 로 지정 : Tab 사용

---

# 반복문

특정한 소스코드를 반복적으로 실행하고자 할 때 사용 (for, while)

### while

```python
i = 1
result = 0

# i가 9보다 작거나 같을 때만 아래 코드를 반복적으로 실행
while i <= 9:
    result += i
    i += 1

print(result)
```
### 반복문에서의 무한 루프

__무한 루프(Infinite Loop)__ 란 끊임없이 반복되는 반복문을 의미하는데, 코딩 테스트에서는 무한 루프를 구현 할 일은 거의 없으며,

반복문을 작성한 뒤에는 항상 반복문을 탈출 할 수 있는 조건이 있는지 확인

```python
# 무한 루프
x = 10

while x > 5:
    print(x)
```

### for

특정한 변수를 이용하여 `in` 뒤에 오는 데이터(리스트, 튜플 등)에 포함되어 있는 원소를 첫 번째 인덱스부터 차례대로 하나씩 방문

```python
array = [9,8,7,6,5]

# for문 기본 예제
# array에 있는 원소들을 하나씩 방문
for x in array:
    print(x)
```

연속적인 값을 차례대로 순회할 때는 `range()` 를 사용하는데, 이 때 `range(start, end+1)` 형태로 사용.

만약에 인자를 하나만 넣으면 자동으로 시작 값은 __0__

```python
result = 0

# i는 1부터 9까지 순회
for i in range(1,10):
    result += i

print(result) # 45
```

### 파이썬의 continue 키워드

반복문에서 남은 코드의 실행을 건너뛰고, 다음 반복을 진행하고자 할 때 사용

```python
result = 0

for i in range(1,10):
    # 짝수일 때 continue를 통해 건너뜀
    if i % 2 == 0:
        continue
    result += i

print(result) # 25
```

### 반복문의 break 키워드

반복문을 즉시 탈출하고자 할 때 사용

```python
i = 1

while True:
    print("현재 i의 값 : ", i)
    if i == 5:
        break

    i += 1
```

---

# 함수 & 람다 표현식

함수(Function)이란 특정한 작업을 하나의 단위로 묶어 놓은 것

함수를 통해 불필요한 코드를 줄일 수 있음

### 함수의 종류

- __내장 함수__ : Python이 기본적으로 제공하는 함수
- __사용자 정의 함수__ : 개발자가 직접 정의하여 사용할 수 있는 함수

### 함수 정의

- __매개 변수__ : 함수 내부에서 사용할 변수
- __반환 값__ : 함수에서 처리 된 결과를 반환

```python
# 함수 포맷
def function_name(parameter): # parameter : 매개 변수
    # Source Code

    return return_value # 반환 값
```

```python
# Sample
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

result = add(3, 7) # 10

print(result)

result = subtract(3, 7) # -4

print(result)
```

### 파라미터 지정하기
파라미터의 경우 변수를 직접 지정할 수 있음 (순서가 달라져도 상관 없음)

```python
def add(a, b):
    print('함수의 결과:', a+b)

add(b = 3, a = 7) # 동일한 결과가 나옴 (10)
```

### Global 키워드 (크게 사용하지 않는 것 같아 보임)

함수의 바깥에 있는 변수를 바로 참조할 경우


```python
a = 0

def func():
    global a
    a += 1
    print(a)
```

### 여러 개의 반환 값

Python에서 함수는 여러 개의 반환 값을 가질 수 있음

```python
def operator(a, b):

    add_var = a + b
    subtract_var = a - b
    multiply_var = a * b
    divide_var = a / b

    # 여러 개의 값 반환
    return add_var, subtract_var, multiply_var, divide_var

a, b, c, d = operator(7, 3)

print(a, b, c, d) # 10 4 21 2
```

### 람다 표현식

함수를 간단하게 작성하기 위해 사용하는데, 특정한 기능을 수행하는 함수를 한 줄에 간단하게 작성할 수 있다는 점이 특징

```python
deff add(a, b):
    return a + b

# 일반적인 add()
print(add(3, 7))

# 람다 표현식
print((lambda a, b: a + b)(3, 7))
```

```python
array [("홍길동", 50), ("이순신", 32), ("아무개", 74)]

def my_key(x):
    return x[1]

print(sorted(array, key=my_key))
print(sorted(array, key=lambda x: x[1])) # Lambda를 활용한 정렬 키 설정 (자주 사용)
```

```python
list1 = [1,2,3,4,5]
list2 = [6,7,8,9,10]

result = map(lambda a, b: a + b, list1, list2) # 같은 길이, 속성의 리스트 끼리의 합

print(list(result)) # [7, 9, 11, 13, 15]
```

---

# 실전에서 유용한 표준 라이브러리

1. __내장 함수__ : 기본 입출력 함수부터 정렬 함수까지 기본적인 함수들 제공 (Python 프로그램을 작성할 때 반드시 필요함)
2. __itertools__ : Python에서 반복되는 형태의 데이터를 처리하기 위한 기능 제공 (특히, 순열과 조합 라이브러리는 코딩 테스트에서 완전탐색 문제로 자주 사용)
3. __heapq__ : 힙(Heap) 자료 구조 제공 (일반적으로 __우선순위 큐__ 기능을 구현하기 위해 사용)
4. __bisect__ : __이진 탐색(Binary Search)__ 기능 제공
5. __collections__ : __덱(Deque)__ , __카운터(Counter)__ 등의 유용한 자료 구조 포함
6. __math__ : 필수적인 수학적 기능 제공 (팩토리얼, 제곱근, 최대공약수, 삼각함수 관련 함수부터 파이와 같은 상수도 포함)

### 자주 사용되는 내장 함수

```python
# sum()
result = sum([1,2,3,4,5])
print(result) # 15

# min(), max()
min_result = min(7,3,5,2)
max_result = max(7,3,5,2)
print(min_result, max_result) # 2 7

# eval() : 사람이 작성하는 형태의 식을 넣었을 때 계산 결과를 반환
result = eval("(3+5)*7")
print(result) # 56

# sorted()
result = sorted([9,1,8,5,4])
reverse_result = sorted([9,1,8,5,4], reverse=True)
print(result) # [1,4,5,8,9]
print(reverse_result) # [9,8,5,4,1]

# sorted() with key
array = [('홍길동', 35), ('이순신', 75), ('아무개', 50)]
result = sorted(array, key=lambda x: x[1], reverse=True)
print(result) # [('이순신', 75), ('아무개', 50), ('홍길동', 35)]
```

### 순열과 조합

모든 경우의 수를 고려해야 할 때 사용

- __순열__ : 서로 다른 n개에서 서로 다른 r개를 선택하여 일렬로 나열 (예: {'A', 'B', 'C'}에서 3개를 선택하여 나열 'ABC', 'ACB', 'BAC', 'BCA', 'CAB', 'CBA')
- __조합__ : 서로 다른 n개에서 순서에 상관 없이 서로 다른 r개를 선택하는 것 (예: {'A', 'B', 'C'}에서 순서를 고려하지 않고 2개를 뽑는 경우 - 'AB', 'AC', 'BC')

순열의 수 : `nPr = n*(n-1)*(n-2)*...*(n-r+1)`

조합의 수 : `nCr = (n*(n-1)*(n-2)*...*(n-r+1)) / r!`

```python
### 순열
from itertools import permutations

data = ['A', 'B', 'C'] # 데이터 준비 (n)

result = list(permutations(data, 3)) # 모든 순열 구하기 (r=3)

print(result)

### 조합
from itertools import combinations

data = ['A', 'B', 'C'] # 데이터 (n)

result = list(combinations(data, 2)) # 2개를 뽑는 모든 조합 (r=2)

print(result)

### 중복 순열
from itertools import product

data = ['A', 'B', 'C'] # 데이터 준비 (n)

result = list(product(data, repeat=2)) # 2개를 뽑는 모든 순열 구하기 (중복 허용)

### 중복 조합
from itertools import combinations_with_replacement

data = ['A', 'B', 'C']

result = list(combinations_with_replacement(data, 2)) # 2개를 뽑는 모든 조합 구하기  (중복 허용)

print(result)
```

### Counter

파이선 Collections 라이브러리의 counter는 등장 횟수를 세는 기능 제공

리스트와 같은 반복 가능(iterable) 객체가 주어졌을 때 내부의 원소가 몇 번씩 등장했는지 알려줌

```python
from collections import Counter

counter = Counter(['red', 'blue', 'green', 'blue', 'blue'])

print(counter['blue']) # blue가 등장한 횟수 : 3
print(counter['green']) # green이 등장한 횟수 : 1
print(dict(counter)) # 사전 자료형으로 출력 : {'red': 2, 'blue': 3, 'green': 1}
```

### 최대 공약수와 최소 공배수

math 라이브러리의 gcd() 함수 이용

```python
import math

# 최소 공배수(LCM)를 구하는함수
def lcm(a, b):
    return a * b // math.gcd(a, b)

a = 21
b = 14

print(math.gcd(21, 14)) # 최대 공약수(GCD) 계산 : 7
print(lcm(21, 14)) # 최소 공배수(LCM) 계산 : 42
```

---

## Reference.

- [동빈나 Youtube : 이코테 2021 1장](https://youtu.be/m-9pAwq1o3w?feature=shared)
