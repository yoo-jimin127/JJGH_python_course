# 이스케이프 코드 : 보기 좋게 문자열을 정리할 수 있는 도구
test_string = "안녕하세요. \n제 이름은 \"유지민\"입니다. \n만나서 반갑습니다."
print(test_string)

# 문자열 연산
head = "Python"
tail = " is fun!"

#문자열 연결
print(head + tail)

#문자열 곱하기
print(head * 5)

#문자열 길이 구하는 함수 : len()
example = "apple banana cat dog egg"
print(len(example))

# 문자열 인덱싱 : 가리킴
a = "Life is too short, You need Python"
print(a[6])

# 문자열 슬라이싱 : 자르다
print(a[0:4]) # 0 부터 4 - 1까지

# 문자열 포매팅
number = 10
name = "pizza"

print("나는 %s를 %d번 먹었다." % (name, number) )

