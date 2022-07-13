



class Circle:
    def __init__ (self, radius):
        self.radius=radius

    def surface (self) :
        return 3.14*(self.radius**2)



a=Circle(2)

print(f"원의 면적: {a.surface()}")


