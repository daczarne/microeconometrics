# Assign a list to an variable named my_list
my_list = [1,2,3]
my_list = ['A string',23,100.232,'o']
len(my_list)

# Indexing and Slicing

my_list = ['one', 'two', 'three', 4, 5]

print("element index 0:", my_list[0])
print("everything starting from index 1:", my_list[1:])
print("everything up to 3:", my_list[:3])

my_list + ['new item']
print(my_list)

# Reassign
my_list += ['add new item permanently']
print(my_list)

my_list * 2
print(my_list)

## List methods

mylist = [1, 2, 3]

# Append
mylist.append('append me!')
print(mylist)

# Pop off the 0 indexed item
mylist.pop(0)
mylist

# Assign the popped element, remember default popped index is -1
popped_item = mylist.pop()
print(popped_item)
print(mylist)

# Indexing will return an error if there is no element at that index
print(mylist[100])

## Nesting lists

lst_1 = [1, 2, 3]
lst_2 = [4, 5, 6]
lst_3 = [7, 8, 9]

# Make a list of lists to form a matrix
matrix = [lst_1, lst_2, lst_3]
print(matrix)
print(matrix[0])
print(matrix[0][0])
