def lowercase_function_name(argument1, argument2, argument3 = 'default value'):
  """
  DocString of the function. It is where you can write a helpful
  description for anyone who will use your function.
  """
  pass


def report_person():
  print("Reporting Person")


report_person()


def report(name):
  print(f"Reporting {name}")


report("James")
report("Bond")


def report(name = "Jason"):
  print(f"Reporting {name}")


report()
report("Kay")


def add(n1, n2):
  print(n1 + n2)


add(2, 3)
result = add(2,3)
print(result)

print(type(result))


def add(n1, n2):
  return n1 + n2

add(2, 3)
result = add(2, 3)
print(result)



def secret_check(mystring):
  return "secret" in mystring

secret_check("This is a secret.")
secret_check("SECRET")


def secret_check(mystring):
  return "secret" in mystring.lower()


secret_check("SECRET!")


def code_maker(mystring):
	output = list(mystring)
	for i, letter in enumerate(mystring):
		for vowel in ["a", "e", "i", "o", "u"]:
			if letter.lower() == vowel:
				output[i] = "x"
	output = "".join(output)
	return output


"".join(["a", "b", "c"])
"--".join(["a", "b", "c"])
"-x-".join(["a", "b", "c"])

code_maker("Edward")
code_maker("John")

print(max(2, 3))
mylist = ["a", "b", "c"]

for x in mylist:
	print(x)


for x in enumerate(mylist):
	print(x)


for i, letter in enumerate(mylist):
	print(i)
	print(letter)
