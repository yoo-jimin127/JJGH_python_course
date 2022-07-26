class Student:
    def __init__(self, score, level):
        self.input_score = score
        self.input_level = level

    def say_hello(self):
        print("저는 %s 학년입니다." % self.input_level)

    def score_upgrade(self):
        self.input_score += 5
        print("문제를 맞췄습니다.")

student1 = Student(50, 1)

print("학년 : ", student1.input_score)
print("점수 : ", student1.input_level)

student1.say_hello()
student1.score_upgrade()

print("학년 : ", student1.input_score)
print("점수 : ", student1.input_level)
