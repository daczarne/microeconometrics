#### Defining a new class ####

# Create a new class called Sample
class Sample():
  pass

# Instance of Sample
x = Sample()
print(type(x))


#### Attributes ####

# Create a new class called Dog
class Dog():
	species = "mammal"
	def __init__(self, breed, name):
		self.breed = breed
		self.name = name

# Create instances of class Dog
my_dog = Dog(breed = "Lab", name = "Sam")

print(my_dog.breed)
print(my_dog.name)
print(my_dog.species)


#### Methods ####

class Circle():
    # This is a Class Object Attribute
    # Notice how it is not under __init__
    pi = 3.14
    # Circle get instantiated with a radius (default is 1)
    def __init__(self, radius = 1):
      self.radius = radius
    # Area method calculates the area. Note the use of self.
    def area(self):
      return self.radius * self.radius * Circle.pi
    # Method for resetting Radius
    def setRadius(self, radius):
      self.radius = radius
    # Method for getting radius (Same as just calling .radius)
    def getRadius(self):
      return self.radius


c = Circle()
c.setRadius(2)
print("Radius is: ", c.getRadius())
print("Area is: ", c.area())


#### Inheritance ####

class Animal():
	def __init__(self, fur):
		self.fur = fur
	def report(self):
		print("Animal")
	def eat(self):
		print("Eating")


class Dog(Animal):
	def __init__(self, fur):
		Animal.__init__(self, fur)
		print("Dog created")
	def report(self):
		print("Dog")
	def bark(self):
		print("Woof!")


d = Dog(fur = "Fuzzy")
d.report()
d.eat()
d.bark()
print(d.fur)


#### Special Methods ####

# Dunder methods
class Book():
	def __init__(self, title, author, pages):
		print("A book is created")
		self.title = title
		self.author = author
		self.pages = pages
	def __repr__(self):
		return f"Title:{self.title}, author:{self.author}, pages:{self.pages}"
	def __len__(self):
		return self.pages


book = Book("Python", "John", 250)

# Special Methods
print(book)
print(len(book))
