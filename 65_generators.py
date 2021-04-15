#%%
"""
Generators
"""
#%%
# Generators are simplified iterators
# Remember our UpToFive class ?
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
for el in u:
	print(el)
# %%
# as a generator
def uptofivegen(value):
	while value <= 5:
		yield value
		value +=1

for el in uptofivegen(0):
	print(el)

#%%
"""
Exercise : rewrite this iterator as a generator (generate rand int until you generate a 9: the 9 must be returned)
"""
import random
class RandomIntIterator:

	def __init__(self):
		self.current_val = None

	def __iter__(self):
		return self

	def __next__(self):
		if self.current_val == 9:
			raise StopIteration
		self.current_val = random.randint(0,10)
		return self.current_val

# %%
r = RandomIntIterator()
for el in r:
	print(el)





















# %%
def randintgenerator():
	while True:
		val = random.randint(0,10)
		yield val
		if val == 9:
			break
# %%
r = randintgenerator()
for el in r:
	print(el)

# %% 
"""Exercise DIFFICULT : transfor this generator into an iterator class"""

def pairwise(items):
	"""Generator that yields two neighbor items from an iterator or iterable.
	Args:
		items: any iterator or iterable
	"""
	iter_items = iter(items)
	curr_item = next(iter_items, None)
	for next_item in iter_items:
		yield curr_item, next_item
		curr_item = next_item
	yield curr_item, None

for el in pairwise([0,1,2,3]):
	print(el)
# %%






















class Pairwise:
	def __init__(self, items):
		self.items = items
		self.it = self.items.__iter__()
		self.curr_item = next(self.it)
	def __iter__(self):
		return self
	def __next__(self):
		iter_items = self.it
		curr_item = self.curr_item
		next_item = next(iter_items, None)
		self.curr_item = next_item
		if curr_item is None:
			raise StopIteration
		return curr_item, next_item

for el in Pairwise([0,1,2,3]):
	print(el)


# %%
