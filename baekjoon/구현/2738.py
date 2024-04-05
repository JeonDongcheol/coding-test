"""
N*M 크기의 두 행렬 A, B의 각각 원소들을 더하기
# 입력
첫째 줄에는 행렬의 크기 N, M (0 < N, M <= 100)
둘째 줄부터 N개의 줄에 A의 원소 M개가 차례대로 주어짐
이어서 B의 원소 M개가 차례대로 주어짐
원소들은 공백을 기준으로 구분되며, 행렬의 원소는 100보다 작거나 같은 정수
"""
n, m = map(int, input().split()) # N, M 입력

a = [] # 행렬 A
b = [] # 행렬 B

# 행렬 원소 입력 받기
for i in range(2):
    for _ in range(n):
        if i == 0:
            a.append(list(map(int, input().split()))) # 각 줄마다 행렬 A의 원소 입력받기
        else:
            b.append(list(map(int, input().split()))) # 각 줄마다 행렬 B의 원소 입력받기

# 행렬 A, B의 원소 값들을 더한 다음, 출력을 위해 문자열 형태로 다시 저장
for i in range(n):
    for j in range(m):
        a[i][j] = str(a[i][j] + b[i][j])

# 출력
for i in a:
    print(" ".join(i))