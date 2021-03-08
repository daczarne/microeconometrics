from models import db, Puppy, Owner, Toy

# Create 2 puppies
rufus = Puppy("Rufus")
fido = Puppy("Fido")

# Add puppies to database
db.session.add_all([rufus, fido])
db.session.commit()

# Print out all the puppies
print(Puppy.query.all())

# Grab Rufus from DB
rufus = Puppy.query.filter_by(name = "Rufus").all()[0]

# Create an owner for Rufus
john = Owner("John", rufus.id)

# Give Rufus some toys
toy1 = Toy("Chew Toy", rufus.id)
toy2 = Toy("Ball", rufus.id)

# Commit these changes to the database
db.session.add_all([john, toy1, toy2])
db.session.commit()

# Grab Rufus again
rufus = Puppy.query.filter_by(name = "Rufus").first()
print(rufus)

# Show toys
rufus.report_toys()


## Delete ##

# find_pup = Puppy.query.get(1)
# db.session.delete(find_pup)
# db.session.commit()
