"""
오늘은 2007년 1월 1일 월요일이다.
그렇다면, 2007년 x월 y일은 무슨요일일까?
# 입력
첫째 줄 : 빈 칸을 사이에 두고 x(1 <= x <= 12)와 y(1 <= y <= 31)이 주어진다.
1,3,5,7,8,10,12 : 31일
4,6,9,11 : 30일
2 : 28일
# 출력
첫째 줄 : x월 y일이 무슨 요일인지에 따라
SUN, MON, TUE, WED, THU, FRI, SAT
# 예시
1 1 -> MON
3 14 -> WED
9 2 -> SUN
12 25 -> TUE
"""

x, y = map(int, input().split()) # x, y 입력받기

# x월 단위로 구분
if x == 2:
    y += 31
elif x == 3:
    y += 31 + 28
elif x == 4:
    y += (31 * 2) + 28
elif x == 5:
    y += (31 * 2) + 30 + 28
elif x == 6:
    y += (31 * 3) + 30 + 28
elif x == 7:
    y += (31 * 3) + (30 * 2) + 28
elif x == 8:
    y += (31 * 4) + (30 * 2) + 28
elif x == 9:
    y += (31 * 5) + (30 * 2) + 28
elif x == 10:
    y += (31 * 5) + (30 * 3) + 28
elif x == 11:
    y += (31 * 6) + (30 * 3) + 28
elif x == 12:
    y += (31 * 6) + (30 * 4) + 28

y %= 7 # y를 7로 나눈 나머지에 따라 요일이 바뀜(0:SUN ~ 6:SAT)

# 결과 출력
if y == 0:
    print("SUN")
elif y == 1:
    print("MON")
elif y == 2:
    print("TUE")
elif y == 3:
    print("WED")
elif y == 4:
    print("THU")
elif y == 5:
    print("FRI")
elif y == 6:
    print("SAT")