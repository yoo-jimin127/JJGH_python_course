# 문자 개수 세는 함수 : count()
a = "banana"
print(a.count('b'))

# 문자 위치를 알려주는 함수 (1) : find()
b = "this is banana"
print(b.find('k'))

# 문자 위치를 알려주는 함수 (2) : index()
print(b.index('k'))

# 문자열 삽입하는 함수 : join()
print("<<<".join("abcde"))

# 소문자 -> 대문자 변경하는 함수 : upper()
c = "hihi"
print(c.upper())

# 대문자 -> 소문자 변경하는 함수 : lower()
d = "STRONG"
print(d.lower())

# 문자열 쓸데없는 공백 지우는 함수
e = "      안녕하세요 공백 많아요     "

# 왼쪽 공백 지우는 함수 : lstrip()
print(e.lstrip())

# 오른쪽 공백 지우는 함수 : rstrip()
print(e.rstrip())

# 왼쪽, 오른쪽 공백을 모두 지우는 함수 : strip()
print(e.strip())

b = "this is banana"

#문자열 바꾸는 함수 : replace()
print(b.replace("banana", "apple"))

# 문자열 나누는 함수 : split()
# print(b.split())
input_value = input("여러분이 좋아하는 음식을 입력해주세요 (그리고로 음식을 구분해주세요): ")
list_value = input_value.split("그리고")
print(list_value)
