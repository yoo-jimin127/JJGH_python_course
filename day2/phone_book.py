phoneBook = {} #전화번호부

# 메뉴 출력 함수
def printMenu():
    line="-----------"
    menu={"1":"추가하기",
            "2":"편집하기",
            "3":"삭제하기",
            "4":"목록보기",
            "5":"종료하기",
        }
    for key in menu:
        print(key , ". " , menu[key])
    print(line)

# 메뉴 입력받는 함수
def inputMenu():
    ans = input("선택할 메뉴는? ")
    return ans

# addBook() : 전화번호를 추가함
def addBook():
    name=input("이름 : ")
    phone=input("전화번호 : ")
    phoneBook[name] = phone
    print(phoneBook)

# editBook() : 전화번호를 편집합
def editBook():
    name=input("편집할 이름 : ")
    if name in phoneBook:
        phone=input("전화번호 : ")
        phoneBook[name] = phone
    else:
        print("--자료 없음--")

# delBook() : 전화번호를 삭제함
def delBook():
    name=input("삭제할 이름 : ")
    if name in phoneBook:
        del(phoneBook[name])
    else:
        print("--자료 없음--")

#viewBook() : 전화번호 목록을 보여줌
def viewBook():
    for name in phoneBook:
        phone=phoneBook[name]
        print(name, ", ", phone)

while True :
    printMenu()
    ans=inputMenu()

    if ans == "1":
        addBook()
    elif ans=="2":
        editBook()
    elif ans=="3":
        delBook()
    elif ans=="4":
        viewBook()
    elif ans=="5":
        break
    else:
        print("다시 선택해 주세요")
