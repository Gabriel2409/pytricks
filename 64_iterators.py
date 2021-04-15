#%%
"""
Basic iterator
Iterator protocol
"""


class Repeater:
	def __init__(self, value):
		self.value = value

	def __iter__(self):
		return self

	def __next__(self):
		return self.value

r = Repeater("my_value")
# %% 
# To implement iterator protocol you need __iter__ and __next__
# ? What will happen here ? 
for el in r:
	print(el)
# %%
# ? What do you think will happen if i comment __iter__ or __next__ ?
next(r) # will it work ? 
#%%
for el in r:
	print(el) # will it work ?
#%%
# Let's decompose
"for el in r" 
iterator = r.__iter__() # or iter(r)
#%%
el = iterator.__next__() # or next(el)
print(el)
#%%
"""iterator = r.__iter__() # or iter(r)
while True:
	el = iterator.__next__() # or next(el)
	print(el)"""
# %%
# * So you really have two steps, the first one is to call the __iter__ method (most of the time you can return the whole object in the iter) and then call the __next__ method several times

#%%
# ! Ok but what about not creating infinite loops ? 

class UpToFive:
	def __init__(self, value):
		self.value = value

	def __iter__(self):
		return self

	def __next__(self):
		if self.value > 5:
			raise StopIteration
		val = self.value
		self.value +=1
		return val

u = UpToFive(0)
# %%
next(u)
# %%
for el in u:
	print(el)
# %%
# it is the same as writing
iterator = iter(u) # same as u.__iter__()
while True:
	try:
		el = next(iterator) # same as iterator.__next__() / Notice that iterator refers to u so it is the same as next(u)
		print(el)
	except StopIteration:
		break
# %%
# * All objects that are iterable are in fact objects that implement the iterator protocol

mylist = [1,2,3]
# %%
next(mylist) # ? what will i get here ? 
# %%
it = iter(mylist)
next(it)
next(it)
next(it)
next(it)
# %%
