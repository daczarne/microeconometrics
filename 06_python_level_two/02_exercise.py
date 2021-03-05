# For this challenge, create a bank account class that has two attributes:
# * owner
# * balance
# and two methods:
# * deposit
# * withdraw
# As an added requirement, withdrawals may not exceed the available balance.
# Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.

class Account:
	def __init__(self, owner, balance = 0):
		self.owner = owner
		self.balance = balance
	def __str__(self):
		return f"Account owner: {self.owner}\nAccount balance: ${self.balance}"
	def deposit(self, dep_amt):
		self.balance += dep_amt
		print("Deposit Accepted")
	def withdraw(self, wd_amt):
		if self.balance >= wd_amt:
			self.balance -= wd_amt
			print("Withdrawal Accepted")
		else:
			print("Funds Unavailable!")


# 1. Instantiate the class
account = Account("Jose", 100)

# 2. Print the object
print(account)

# 3. Show the account owner attribute
print(account.owner)

# 4. Show the account balance attribute
print(account.balance)

# 5. Make a series of deposits and withdrawals
account.deposit(50)
account.withdraw(75)

# 6. Make a withdrawal that exceeds the available balance
account.withdraw(500)
