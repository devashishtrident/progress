#tuples
'''tuples are represented via brackets and are just like LIST it can have different items'''
t =(1,2,3)
print(t[0])
t = ('a',True,123)
print(t)
'''tuples are immutable'''
#t[0]='NEw'
#sets
'unique item is always  returned SETS return unsorted item'
x = set()
x.add(1)
x.add(2)
x.add(3)
x.add(0.1)
x.add(4)
x.add(4)
x.add(4)

print(x)

#list of repeated elements can be removed
converted = set([1,1,1,1,1,1,2,2,2,2,3,3,3,3])
print(converted)
