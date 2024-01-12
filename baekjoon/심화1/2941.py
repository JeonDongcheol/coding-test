"""
크로아티아 알파벳

- č : c=
- ć : c-
- dž : dz=
- đ : d-
- lj : lj
- nj : nj
- š : s=
- ž : z=
* 모두 하나의 알파벳, 나머지는 하나씩 계산

입력 : 최대 100글자의 단어 (알파벳 소문자, -, =)
출력 : 몇 개의 크로아티아 알파벳으로 구성되어있는지 계산

ex) ljes=njak : 6
"""

CONVERT_STRING = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="] # 크로아티아 문자

convert_result = input()

for convert_string in CONVERT_STRING:
    # 크로아티아 문자가 있다면,
    if convert_string in convert_result:
        convert_result = convert_result.replace(convert_string, "o") # 상관 없는 문자로 치환

print(len(convert_result))