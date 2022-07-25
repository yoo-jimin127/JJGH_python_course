def cal(a, b, oper):
    if oper == "덧셈":
        result = a + b

    elif oper == "뺄셈":
        result = a - b

    elif oper == "곱셈":
        result = a * b

    elif oper == "나눗셈":
        result = a / b
    else :
        print("지원하지 않는 메뉴입니다.")
        return 0

    return result

num1 = int(input("첫번째 숫자를 입력하세요 : "))
num2 = int(input("두번째 숫자를 입력하세요 : "))
user_oper = input("연산을 입력하세요 : ")

print("결과 값 : ", cal(num1, num2, user_oper))
