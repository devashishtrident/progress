#concept revisions
'''
if 1 < 2:
    if 2 < 3:
        print("True!")

if 1 < 2:
    print("First Block")
    if 20< 3 :
        print("second BLock")

if 1 < 2 :
    print("hello")
'''
#####################################################
seq = [1,2,3,4,5,6]
for item in seq :
    print("hello")
'''calling for loop on a dictionary-----> it print out the keys not the values dictionary dont return certain order '''
d = {"sam":1,"Frank":2,"Dan":3}

for item in d:
    print(item)

''''to get the value for each key'''
for k in d:
    print(k)
    print(d[k])
'''methods you can use to call the values are d.keys or d.values'''
#####################################################################################################
'''iterating through tuples and packing the tuples
inside list you will be provided with the tuples'''
#i've a list of 3 tuples
mypairs = [(1,2),(3,4),(5,6)]
for item in mypairs:
    print(item) #here i got the value of full tuples like (1,2) (3,4) (5,6)
'''to unpack the tuple'''
for (tup1,tup2) in mypairs:
    print(tup1)
    print(tup2)

#########################################################
i=1
while i < 5:
    print("i is : {}".format(i))
    i  = i+1

"""how does range works:
list(range(0,5))---> returns [0,1,2,3,4]
list(range(0,20,2))---> returns [0,2,4,6,8,10,12,14,16,18]"""
x = [1,2,3,4]
out =[]
for num in x:
    out.append(num**2)
print(out)
'''or append ka formulae'''
out = [num**2 for num in x]
print(out)



























