"""
문제 : 별 찍기 (심화)

입력 : 첫째 줄에 N(1 <= N <= 100)

출력 : 2*N-1번까지 차례대로 별 출력

ex)
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *

핵심
1. 규칙성 찾기
- 공백 : For Loop를 돌면서 절댓값 (N - index) - 1
- 별
    - index가 N보다 작거나 같을 때 : (2 * index) - 1
    - index가 N보다 클 때 : (2 * (2 * N) - index) - 1
"""
STAR = "*"
SPACE = " "

n = int(input()) # N input

for i in range(1, (n*2)):
    space = SPACE * abs(n - i) # 공백 규칙은 동일

    # index가 N보다 작거나 같은 경우
    if i <= n:
        star = (STAR * 2 * i)[:-1] # [:-1] : String 배열 마지막 원소 삭제
    # index가 N보다 큰 경우
    else:
        star = (STAR * (2 * ((2*n) - i)))[:-1]

    print(space + star)