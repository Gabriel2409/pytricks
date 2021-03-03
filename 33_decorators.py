# %% property decorator : useful to protect a var
# https://stackoverflow.com/questions/17330160/how-does-the-property-decorator-work-in-python
class House:

	def __init__(self, price, readonly):
		self._price = price
		self._readonly = readonly

	@property
	def price(self):
		return self._price

	@price.setter
	def price(self, new_price):
		if new_price > 0 and isinstance(new_price, float):
			self._price = new_price
		else:
			print("Please enter a valid price")

	@price.deleter
	def price(self):
		del self._price

	@property
	def readonly(self):
		return self._readonly

h = House(100, "do not change")
dir(h)
# %%
h.price
# %%
del h.price

# %%
print(h.readonly)
# %%
h.readonly = 15 # i cant change it
# %%
del h.readonly # i cant delete it
# %%
h._readonly = 18 # i can still do it by accessing the private var : remember the _ is only there to communicate intent. 
print(h.readonly)
# %%
