"""
전공 평점 계산

* 전공 평점 : 전공 과목별 (학점 * 과목평점)의 합을 학점의 총합으로 나눈 값

- 등급에 따른 과목 평점
A+ : 4.5
A0 : 4.0
B+ : 3.5
B0 : 3.0
C+ : 2.5
C0 : 2.0
D+ : 1.5
D0 : 1.0
F : 0.0
P : 계산에서 제외

입력 : 20줄에 걸쳐 수강한 전공 과목의 과목명, 학점, 등급이 공백으로 구분
출력 : 전공 평점 (절대오차 | 상대오차 10^-4 이하)

제한
1. 1 <= 과목명의 길이 <= 50
2. 과목명 : 알파벳 대소문자 혹은 숫자 (띄어쓰기 없으며, 과목명은 서로 다름)
3. 학점 : 1.0, 2.0, 3.0, 4.0 중 하나
4. 등급 : A+, A0, B+, B0, C+, C0, D+, D0, F, P 중 하나
5. 적어도 한 과목은 등급이 P가 아님 -> 모두 계산에서 제외되는 경우는 없음
"""

total_point = 0.0 # (학점 * 과목평점)의 총합
total_credit = 0.0 # 학점의 총합

# 학점에 따른 과목 평점
point_by_grade = {
    "A+": 4.5,
    "A0": 4.0,
    "B+": 3.5,
    "B0": 3.0,
    "C+": 2.5,
    "C0": 2.0,
    "D+": 1.5,
    "D0": 1.0,
    "F": 0.0
}

for i in range(0, 20):
    subject = input()

    subject = subject.split(" ") # 공백으로 구분(0: 과목명, 1: 학점, 2: 등급)

    # 학점이 P인 경우 계산에서 제외
    if subject[2] == "P":
        continue

    total_credit += float(subject[1]) # 학점의 총합 계산

    total_point += float(subject[1]) * float(point_by_grade[subject[2]])  # 학점 * 과목평점 계산

# 전공 평점 계산
print(total_point/total_credit)

