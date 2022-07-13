



class Person():
    def __init__(self):
        pass

    def getGender(self):
        return "Unknown"



class Male(Person):
    def __init__(self):
        self.gender = "Male"

    def getGender(self):
        return self.gender

        
class Female(Person):
    def __init__(self):
        self.gender = "Female"

    def getGender(self):
        return self.gender



print(Male().getGender())

print(Female().getGender())