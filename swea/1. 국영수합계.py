



class student():
    def __init__(self, korean, english, math):
        self.korean = korean
        self.english = english
        self.math = math

    def total(self) :
        print(f"국어, 영어, 수학의 총점: {self.korean + self.english +self.math}")




a, b, c = map(int, input().split(", "))


student(a, b, c).total()