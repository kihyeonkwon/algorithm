



class Square():
    def __init__(self, length, height):
        self.length=length
        self.height=height
    
    def area(self):
        return self.length * self.height



a=Square(4,5)

print(f'사각형의 면적: {a.area()}')
