"""
그룹 단어 : 단어에 존재하는 문자에 대해서, 각 문자가 연속해서 나타나는 경우
ex) aaabbbbccc : 그룹 단어, aabbba : 그룹 단어 X

단어 N개 입력 받고 그룹 단어의 개수 출력

입력
- 첫째 줄 : 단어 개수 N
- 둘째 줄부터 N개의 줄 : 단어 (알파벳 소문자, 중복 X, 최대 길이 : 100)
출력 : 그룹 단어 개수
"""

n = int(input())

count = 0

for i in range(n):
    is_jumped = False # 알파벳을 건너뛰었는지 여부 판단하기 위한 Boolean
    is_group_word = True # 그룹 단어인지 판단하기 위한 Boolean

    input_str = input()

    # Target 알파벳과 해당 알파벳 이후의 알파벳을 탐색하기 위한 Index
    for i, target_str in enumerate(input_str):
        # Target 알파벳 이후부터 그룹 단어 여부 체크
        for k in range(i+1, len(input_str)):
            # Target 알파벳과 같지 않다면, 건너뜀 : 건너뛰었다는 것을 표시하기 위해 is_jumped를 True로 바꿈
            if target_str != input_str[k]:
                is_jumped = True
            # 건너뛰었는데 같은 알파벳이 존재한다면 그룹 단어가 아닌 것이 판단이 가능하기 때문에 Loop에서 빠져나감
            elif is_jumped and target_str == input_str[k]:
                is_group_word = False
                break

        # 모두 돌았을 때 그룹 단어가 아니라면 굳이 다음 Target 알파벳을 탐색하지 않음
        if not is_group_word:
            break

        # 해당 Target 알파벳에 대해 작업이 끝나면 Boolean 변수를 초기화
        is_jumped = False
        is_group_word = True

    # 최종적으로 그룹 알파벳이라고 판단되면 count +1
    if is_group_word:
        count += 1

print(count)
