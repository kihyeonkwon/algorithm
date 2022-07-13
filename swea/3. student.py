




class Student :
    def __init__(self, name):
        self.__name = name

    @property
    def name (self):
        return self.__name






class GraduateStudent(Student):


    def __init__(self, name, major):
        Student.__init__(self, name)
        self.__major = major




    @property
    def major(self):
        return (f'이름: {self.name}, 전공: {self.__major}')

    

a=Student('홍길동')

print("이름: " + a.name)

b=GraduateStudent('이순신', '컴퓨터')

print(b.major)