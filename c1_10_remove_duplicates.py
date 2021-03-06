#%% remove duplicate
"""
sets
hashable
unhashable with key
"""


#%%
# hashable types

print(set([45,0,0,45,3,2,5,2,3]))
# order is not kept
#%%
# solution : create a generator that yields the next item of my iterable on certain conditions
def dedupe(items):
	seen = set()
	for item in items:
		if item not in seen:
			yield item
			seen.add(item)

print(list(dedupe([99, 1,2,3,4,5,4,5,4,5,4,3,5,2,10])))

# %%
# unhashable type
set(({"a":1}, {"a":1}, {"a":2}))
# %%
list(dedupe([{"a":1}, {"a":1}, {"a":2}]))
# %%
# let's modify our dedupe function
def dedupe(items, key=None):
	seen = set()
	for item in items:
		val = item if key is None else key(item)
		if val not in seen:
			yield item
			seen.add(val)
# %%
list(dedupe([{"a":1}, {"a":1}, {"a":2}], key = lambda x: x["a"]))
#%%
import operator
class Car:
	def __init__(self, name, color):
		self.name = name
		self.color = color
	def __repr__(self):
		return f"<Car: {self.name} of color {self.color}>"

a = Car("BMW", "blue")
b = Car("Audi", "blue")
c = Car("BMW", "green")
d = Car("BMW", "blue")
#%%
print(list(dedupe([a, b, c, d])))
#%%
print(list(dedupe([a, b, c, d], key= operator.attrgetter("color"))))
#%%
print(list(dedupe([a, b, c, d], key= operator.attrgetter("name"))))
#%%
print(list(dedupe([a, b, c, d], key= operator.attrgetter("name", "color"))))

# %%
tboxlist = []
textboxes = ["tbox1", "tbox2", "tbox3", "tbox4", "tbox4", "tbox1", "tbox6"]
for tbox in dedupe(textboxes):
	tboxlist.append(tbox)
print(tboxlist)


# %%
