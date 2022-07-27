def introduce_myself(name, gender, age=17, addr="Incheon"):
    print("당신의 이름은 ", name, "입니다.")
    print("당신은 ", age, "세", gender, "입니다.")
    print("당신은 ", addr, "에 삽니다.")

name=input("이름 : ")
gender=input("성별 : ")
age=input("나이 : ")
addr=input("사는 지역 : ")

introduce_myself(name, gender, age, addr)
introduce_myself(name, gender, age)
introduce_myself(name, gender)
