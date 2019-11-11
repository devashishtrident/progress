'''x =25
def my_func():
    x = 50
    return x
"/the only x the program is aware of is global variable"
#print(x)
"this is looking at the myfunc scope only"
#print(my_func())
"what confuses the people most is calling the function first and getting the very next value we get x will be called but a global variable not the
myfunc vaala"
my_func()
print(x)
'''
'''lets create a lambad expression'''
'''
lambda x : x**2


#enclosing functional locals

name = 'this is a global name!'

def greet():
    name = "sammy"
    "it worked only because hello function was called inside greet not inside hello since that will throw an error"

    def  hello():
        print("hello "+name)
    hello()

greet()
"but if i ask name to be print seperatley it wont go inside since it have no business inside the scope
""
print(name)
#####################################################built in functions'''
x =50
def func(x):
    print('x is :',x)
    x = 1000
    print('local x changed to:',x)

func(x)
print(x)
#only above value is considered in these for
#eg: x defined in func x still refers to above global x and after x changed it refers to it but
#x scope was only inside the function but after that the x got reverted back to 50


#global keyword is not recommended to use
y = 50

def func():
    global y
    y =1000


print("before function call,y is:",y)
func()
print("after function call,y is:",y)
######################################################################################################################################











































































