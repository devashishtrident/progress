class Circle():
    pi = 3.14
    def __init__(self,radius=1):
        self.radius = radius
    def area(self):
        return self.radius*self.radius*Circle.pi
    def set_radius(self,new_r):
        self.radius = new_r


'''just like method we have to mention the () brackets calling a function from a class'''


myc = Circle(3)
myc.set_radius(999)
print(myc.area())


