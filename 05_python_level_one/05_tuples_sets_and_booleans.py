#### Tuples ###

t = (1, 2, 3)
len(t)

t = ('one', 2)
print(t)

print(t[0])

print(t[-1])

## Tuple methods

print(t.index('one'))
print(t.count('one'))

t[0] = 'change'
t.append('nope')
print(t)

#### Sets ####

x = set()
x.add(1)
print(x)

x.add(2)
print(x)

x.add(1)
print(x)

# Create a list with repeats
mylist = [1, 1, 2, 2, 3, 4, 5, 6, 1, 1]
# Cast as set to get unique values
set(mylist)
print(mylist)

#### Booleans ####

a = True
print(a)

print(1 > 2)

# None placeholder
b = None
