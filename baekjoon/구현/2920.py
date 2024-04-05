"""
다장조 : c d e f g a b C (8개)
c = 1, d = 2, ... C = 8
1부터 8까지 연주하면 ascending, 8부터 1까지 연주하면 descending, 둘 다 아니라면 mixed
셋 중에 하나 판단하기
# 입력
첫째 줄 : 8개 숫자
# 출력
ascending, descending, mixed 중에 출력
"""
list_num = list(map(int, input().split())) # 음정 받기

# ascending, descending 판별 Boolean
ascending = True
descending = True

for i in range(8):
    # 원소 하나라도 값이 index + 1이 아니라면 ascending이 아님
    if list_num[i] != (i + 1):
        ascending = False
    # 원소 하나라도 값이 8 - index가 아니라면 descending이 아님
    if list_num[i] != (8 - i):
        descending = False

    # 둘 다 아닌 것이 판단 되었으면 더 이상 반복문을 수행하지 않음
    if not ascending and not descending:
        break

# 출력
if ascending:
    print("ascending")
elif descending:
    print("descending")
else:
    print("mixed")