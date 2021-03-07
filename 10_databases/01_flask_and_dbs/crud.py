from app import db, Puppy


#### CREATE ####

# Create new entry with name Rufus and age 5
my_puppy = Puppy("Rufus", 5)
db.session.add(my_puppy)
db.session.commit()


#### READ ####

# Grab all puppies
all_puppies = Puppy.query.all()
print(all_puppies)
print("\n")

# Grab by id
puppy_one = Puppy.query.get(1)
print(puppy_one)
print(puppy_one.age)
print("\n")

# Filters
puppy_sam = Puppy.query.filter_by(name = "Sammy") # Returns list
print(puppy_sam)
print("\n")


#### UPDATE ####

# Change the age of puppuy with id = 1
first_puppy = Puppy.query.get(1)
first_puppy.age = 10
db.session.add(first_puppy)
db.session.commit()


#### DELETE ####

# Delete the puppy with id = 2
second_pup = Puppy.query.get(2)
db.session.delete(second_pup)
db.session.commit()


# Check for changes:
all_puppies = Puppy.query.all() # list of all puppies in table
print(all_puppies)
