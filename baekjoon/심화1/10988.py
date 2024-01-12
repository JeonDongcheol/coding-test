"""
알파벳 소문자로만 이루어진 단어
-> 해당 단어가 팰린드롬인지 확인
* 팰린드롬 : 앞으로 읽을 때와 거꾸로 읽을 때 똑같은 단어
ex) level, noon ...

입력 : 단어 (길이 1~100)
출력 : 1(True), 0(False)
"""

input_str = input()

output = []

for string in input_str:
    output.append(string) # String 문자 하나씩 배열로 input

output.reverse() # 거꾸로 뒤짚기 (변수 선언하지 않아도 된다.)

output = "".join(output) # join을 통해 배열 문자 조합

if output == input_str:
    print(1)
else:
    print(0)