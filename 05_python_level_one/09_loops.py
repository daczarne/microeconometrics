#### for loops ####

seq = [1, 2, 3, 4, 5]

for item in seq:
	print(item)


for item in seq:
	print('Yep')


# You can call the loop variable whatever you want:
for jelly in seq:
	print(jelly + jelly)


ages = {
  "Sam": 3,
  "Frank": 4,
  "Dan": 29
}

for key in ages:
  print("This is the key")
  print(key)
  print("This is the value")
  print(ages[key])
  print("\n")


mypairs = [
	(1, 10),
	(3, 30),
	(5, 50)
]


for tup in mypairs:
    print(tup)


for item1, item2 in mypairs:
	print(item1)
	print(item2)


#### WHILE LOOPS ####

i = 1
while i < 5:
  print('i is: {}'.format(i))
  i = i+1

#### RANGE FUNCTION ####

# Note that its a generator:
range(5)

list(range(5))

for i in range(5):
  print(i)


# Start and ending
print(range(1, 10))

# Third argument for step-size
print(range(0, 10, 2))
