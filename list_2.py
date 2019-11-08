'''printing via index in nested loops'''
my_list = [1,2,['x','y','z']]
print(my_list[2])
'''i want to print y only'''
print(my_list[2][1])

matrix = [[1,2,3],[4,5,6],[7,8,9]]
matrix[0][0]


'''LIST COMPREHENSION FLAT FOR LOOP!!!!!!!!
grab 1st element in loop-->row[0]
and for row iterates over matrix'''
first_col= [row[0] for row in matrix]
print(first_col)
