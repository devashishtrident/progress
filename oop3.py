#inheritance
class Animal():


    def __init__(self):
        print("ANIMAL CREATED")

    def whoAmI(self):
        print("ANIMAL")

    def eat(self):
        print("EATING")

class Dog(Animal):
    def __init__(self):
       # Animal.__init__(self)
        print("DOG CREATED")

    def bark(self):
        print("WOOF")

    def eat(self):
        print("dog eating bruh!!!")



mydog = Dog()
mydog.whoAmI()
mydog.bark()
mydog.eat()



