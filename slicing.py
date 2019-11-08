'''slicing of strings is here'''

mystring = 'abcdefg'

print(mystring[2:])
'''it will grab upto specified index(not including) i.e excluding mentioned index'''
print(mystring[:3])
'''grab letter cde'''
print(mystring[2:5])
'''to grab everything in a string use :: or :   '''
print(mystring[::])
'''to select via steps to select the given strings 2-->means every other item from current index to specified jumps  '''
print(mystring[::2])
'''strings are immutable THIS WILL THROW AN ERROR HERE SINCE STRINGS ARE IMMUTABLE'''
#mystring[0] = 'X'
#####################################################################################################
'''basic string methods predefined-->converts to uppercase'''
x=mystring.upper()
print(x)
y = mystring.lower()
print(y)
'''returns 1st letter capital that's it!'''
x=mystring.capitalize()
print(x)
#########################################################################
'''SPLIT METHOD---> defaults split do in space '''
mystring = 'Hello world'
x = mystring.split()
print(x)
y=mystring.split('e')
print(y)
z = mystring.split('o')
print(z)


