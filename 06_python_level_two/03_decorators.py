### Functions within functions ###

def hello(name = "Jose"):
	print("The hello() function has been executed")
	def greet():
		return "\t This is inside the greet() function"
	def welcome():
		return "\t This is inside the welcome() function"
	print(greet())
	print(welcome())
	print("Now we are back inside the hello() function")


### Returning Functions ###

def hello(name = 'Jose'):
	print("The hello() function has been executed")
	# Greet function
	def greet():
		return "\t This is inside the greet() function"
	# Welcome function
	def welcome():
		return "\t This is inside the welcome() function"
	# Return a function
	if name == "Jose":
		return greet
	else:
		return welcome

# Returns the greet function
x = hello()
print(x())

# Return the welcome function
x = hello(x = "Sammy")
print(x())


### Functions as arguments ###

def hello():
	return "Hi Jose!"


def other(func):
	print("Other code would go here")
	# Assume that func is a function and it can be called
	print(func())

other(hello)


### Decorator ###

def new_decorator(func):
	def wrap_func():
		print("Some code bebofre calling func")
		func()
		print("Code after calling func")
	return wrap_func


def func_needs_decorator():
  print("Please decorate me")


# Run the function
func_needs_decorator()

# Reassign func_needs_decorator
func_needs_decorator = new_decorator(func_needs_decorator)
func_needs_decorator()


# Decorator syntax
@new_decorator
def func_needs_decorator():
  print("This function is in need of a Decorator")

func_needs_decorator()
