#%%
def outer(myvar):
	def inner():
		print(myvar)
	print(myvar)
	inner()
	print(myvar)

outer(myvar="outer")
# %%
def outer(myvar):
	def inner():
		myvar = "inner"
		print(myvar)
	print(myvar)
	inner()
	print(myvar)

outer(myvar="outer")
# %%
def outer(myvar):
	def inner():
		print(myvar)
		myvar = "inner"
	print(myvar)
	inner()
	print(myvar)

outer(myvar="outer")

# There is an error because myvar is defined in the scope of the inner function; So python first looks in this scope and sees that the var is printed before assignment
# %%
def outer(myvar):
	def inner():
		nonlocal myvar
		myvar = "inner"
		print(myvar)
	print(myvar)
	inner()
	print(myvar)

outer(myvar="outer")

# Successfull modification of myvar
# %%
def outer(myvar):
	def inner():
		nonlocal myvar
		print(myvar)
		myvar = "inner"
	print(myvar)
	inner()
	print(myvar)

outer(myvar="outer")

# No more error
# %%
def outer(myvar):
	def inner1():
		def inner2():
			nonlocal myvar
			myvar = "inner2"

		print(myvar)
		inner2()
		print(myvar)


	print(myvar)
	inner1()
	print(myvar)

outer(myvar="outer")

# %%
def outer(myvar):
	def inner1():

		myvar = "inner1"
		def inner2():
			nonlocal myvar
			myvar = "inner2"

		print(myvar)
		inner2()
		print(myvar)


	print(myvar)
	inner1()
	print(myvar)

outer(myvar="outer")
# %%
def outer(myvar):
	def inner1():
		def inner2():
			nonlocal myvar
			myvar = "inner2"

		nonlocal myvar
		myvar = "inner1"
		print(myvar)
		inner2()
		print(myvar)


	print(myvar)
	inner1()
	print(myvar)

outer(myvar="outer")
# %%
from functools import wraps

def argumentor(myvar):
	def decorate(func):
		@wraps(func)
		def wrapper(*args, **kwargs):
			nonlocal myvar
			print("myvar", myvar)
			myvar = myvar + 1
			func(*args, **kwargs)
		return wrapper
	return decorate

@argumentor(0)
def passtime():
	for _ in range(1000):
		pass
#%%
passtime()
# %%
# * Conclusion : nonlocal accesses the outer scope of the inner function. It is not greedy (it stops in the closest enclosing func containing the var)
# * note : as long as you don't reassign the var in the inner function, you can still get it without nonlocal (see first example with print)
