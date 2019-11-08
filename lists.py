'''LISTS ARE PYTHON'S FORM OF ARRAYS
list are cretaed using square brackets []
note:lists are mutable'''
###########################################
'''
#mylist =[1,2,3]
mylist = ['stringadgasfd',1,2,3,23.2,True,'asdf',[1,2,3]]
print(mylist)
print(len(mylist))
'''
mylist = ['a','b','c','d','e']
print("before assignment")
print(mylist)
print(mylist[0])
print(mylist[-1])
#from 1 to end
print(mylist[1:])
#from beginning but upto 3 i.e 2
print(mylist[:3])
############################################################################
''' list are mutable '''
print("after assignment")
mylist[0 ]= "NEW ITEM"
print(mylist)
'''mylist append // appends item in the last of a list '''
mylist.append("NEW ITEM")
print(mylist)
'''list inside a list'''
mylist.append(["x","y","z"])
print(mylist)
'''or if you want to make one list a part ..use "EXTENDS METHOD"'''
listtwo = ["x","y","z"]
mylist.extend(listtwo)
print(mylist)
'''to remove something fom list use POP'''
mylists = ['a','b','c','d','e']
item = mylists.pop()
print(mylists)
print(item)
'''specifying index to pop'''
itemtwo = mylists.pop(0)
print(itemtwo)
'''use reverse method to reverse a string'''
mylists.reverse()
print(mylists)
'''sorting a list here'''
mylist = [4,6,7,43,2,1]
mylist.sort()
print(mylist)































