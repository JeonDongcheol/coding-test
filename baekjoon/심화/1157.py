"""
알파벳 대소문자로 된 단어
가장 많이 사용된 알파벳 구하기 (대소문자 구분하지 않음)

입력 : 알파벳 대소문자로 이루어진 단어 (단어 길이 < 1,000,000)
출력 : 가장 많이 사용된 알파벳을 대문자로 출력, 여러 개일 경우 ?

ex)
Mississipi : ?
zZa : Z
z : Z
"""

# 대문자 ASCII Code : A(65) ~ Z(90)

CHARACTER = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] # 알파벳 Count

input_str = input().upper() # 모두 대문자로 변환

# 알파벳 Count 계산
for string in input_str:
    # Index를 찾기 위해 ASCII Code 반환 후 대문자 ASCII 시작 수(65)만큼 빼기
    idx = ord(string) - 65

    CHARACTER[idx] += 1 # 해당 알파벳 Index + 1

max_count = 0
max_alphabet = "?"

for alphabet_idx, count in enumerate(CHARACTER):
    # 새로운 비교대상인 count가 더 크다면,
    if max_count < count:
        max_count = count # max_count 교체
        max_alphabet = chr(alphabet_idx + 65) # Alphbet Index에 65를 다시 더해서 문자로 반환
    # MAX Count가 같다면 : ?
    elif max_count == count:
        max_alphabet = "?"

print(max_alphabet)
