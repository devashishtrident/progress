#task1
s = 'django'
print(s[0])
print(s[5])
print(s[-1])
print(s[:4])
print(s[1:4])
print(s[4:])
print(s[::-1])
#task2
l = [3,7,[1,4,'hello']]
l[2][2] = 'goodbye'
#task3 grab the hello from dictionaries
d1 ={'simple_key':'hello'}
print(d1['simple_key'])
d2 = {'k1':{'k2':'hello'}}
print(d2['k1']['k2'])
d3 = {'k1':[{'nest_key':['this is deep',['hello']]}]}
'''list you select via index not key'''
print(d3['k1'][0]['nest_key'][1])
#task4
mylist = [1,1,1,1,1,1,1,1,1,1,1,1,1,2,3,3,4,4,5,7]
unique_values=set(mylist)
print(unique_values)
#task5
age = 4
name = 'sammy'
print("Hello my dog's name is {a} and he's {b} years old".format(b=age,a=name))