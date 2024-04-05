"""
세 정수 A, B, C 중에서 두 번째로 큰 정수 출력
# 입력
첫째 줄 : A, B, C 공백으로 구분하여 출력 (1 <= A, B, C <= 100)
# 출력
두 번째로 큰 정수 출력
"""

# A, B, C 입력 -> 공백으로 구분하여 List 형태로 선언
list_num = list(map(int, input().split()))

list_num.sort() # 순서대로 정렬

print(list_num[1]) # 두 번째 수 출력