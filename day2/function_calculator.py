def calculator_jj(num1, num2, oper):
  if oper == "+":
    return num1 + num2
  elif oper == "-":
    return num1 - num2
  elif oper == "*":
    return num1 * num2
  elif oper == "/":
    return num1 / num2
  else :
    return "지원하지 않는 연산자"

user_num1 = int(input("첫번째 숫자를 입력하세요 : "))
user_num2 = int(input("두번째 숫자를 입력하세요 : "))
user_oper = input("연산자를 입력하세요 : ")

result = calculator_jj(user_num1, user_num2, user_oper)
# 2 + 3 = 5
print(user_num1,user_oper, user_num2, "=", result)
