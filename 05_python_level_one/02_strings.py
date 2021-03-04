print('hello')
print('This is also a string')
print("String built with double quotes")
print("I'm using single quotes, but will create an error")
print("Now I'm ready to use the single quotes inside a string!")
print('Hello World')
print('Hello World 1')
print('Hello World 2')
print('Use \n to print a new line')
print('\n')

# String Basics
print(len('Hello World'))

# Assign s as a string
s = 'Hello World'
print(s)

# Show first element (in this case a letter)
print("first letter:", s[0])

# Next element
print("second letter:", s[1])

# Next Element
print("third letter:", s[2])

# Slicing
print("second - last:", s[1:])
print("first to fourth:", s[:3])
print("entire string:", s[:])
print("last letter:", s[-1])
print("everthing but the last:", s[:-1])

# Grab everything, but go in steps size of 1
print("steps by 1:", s[::1])

# Grab everything, but go in step sizes of 2
print("steps by 2:", s[::2])

# We can use this to print a string backwards
print("backwards:", s[::-1])


## String Properties

print(s)
s[0] = 'x'
print(s)

s + ' concatenate me!'
s += ' concatenate me!'
print(s)

letter = 'z'
letter*10

## String methods

print(s)
print(s.upper())
print(s.lower())
print(s.split())
print(s.split('W'))

## f strings

print('Insert another string with curly brackets: {}'.format('The inserted string'))
print('This is a string with an {p}'.format(p = 'insert'))
print('One: {p}, Two: {p}, Three: {p}'.format(p = 'Hi!'))
print('Object 1: {a}, Object 2: {b}, Object 3: {c}'.format(a = 1, b = 'two', c = 12.3))
username = "Jose"
color = "Blue"
print(f"The name is {username} and color is {color}")
