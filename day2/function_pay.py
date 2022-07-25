def computepay(hour, pay) :
    if hour > 40 :
        remainder_hour = hour - 40
        total_pay = (hour * pay) + (remainder_hour * pay * 1.5)

    else :
        total_pay = hour * pay
    
    return total_pay

user_hour = int(input("일 한 시간을 입력하세요 : "))
user_pay = int(input("시급을 입력하세요 : "))
print("당신의 월급은 %d원 입니다." %computepay(user_hour, user_pay))
