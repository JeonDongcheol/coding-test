"""
첫째 줄에는 별 N개, 둘째 줄에는 별 N-1개, N번째 줄에는 별 1개 출력
오른쪽 정렬하여 출력
# 입력
첫째 줄 : N(1 <= N <= 100)
# 출력
오른쪽 정렬하여 차례대로 별 출력
"""

n = int(input()) # N 입력

for i in range(n):
    # 공백을 우선 출력 후 * 출력
    print((" " * i) + ("*" * (n - i)))