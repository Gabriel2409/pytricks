#%%
"""
classes without repr and str
repr 
repr + str
"""
#%%
#* no repr
class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y

a = Point(1,0)
print(a)
a
# %%
# * repr but no str
class Pointv2(Point):
	def __repr__(self):
		return f"x={self.x}, y={self.y}"

b = Pointv2(2,3)
print(b)
b
# %%
# * repr and str
class Pointv3(Pointv2):
	def __str__(self):
		return f"x has a value of {self.x} and y has a value of {self.y}"

c = Pointv3(5,6)
print(c)
c
# %%
# * what happens when i write print(c)
c.__str__()
# %%
c.__repr__()
# %%
print(f"{c}")
# %%
print(f"{c!s}")

# %%
print(f"{c!r}")
# %%
# * str but no repr

class Pointv4(Point):
	def __str__(self):
		return f"x is {self.x} and y is {self.y}"

d = Pointv4(9,8)
print(d)
print(f"{d!r}")
# %%
# ! CONCLUSION : ALWAYS DEFINE REPR


#%% Bonus 

class FormattedNumber:
	def __init__(self, number):
		self.number = number

	def __repr__(self):
		return f"{self.number:,}"

print(FormattedNumber(3764324567654))
# %%
# Note : this is completely overkill. 
# You could just do
print(f"{3764324567654:,}")
# Moreover it is a bad practice to mix repr and formatting as there is a format method for this. 
# See next lesson
# %%
