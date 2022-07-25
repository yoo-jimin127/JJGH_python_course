hours = int(input("근무 시간을 입력하세요 : "))
pay = 9160

if hours > 40 :
    total_pay = 9160 * hours * 1.5

else :
    total_pay = 9160 * hours

print("당신의 이번달 월급은 ", total_pay, "입니다.")
