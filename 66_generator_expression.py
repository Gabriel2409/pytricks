#%%
"""
Generator expressions
Chaining generator
"""
#%%

#
[i for i in range(10)]
# %%
(i for i in range(10))

# %%
mygen = (i for i in range(10))

# %%
for el in mygen:
	print(el)
# %%
# syntactic sugar 
sum([i for i in range(10)])
# %%
sum((i for i in range(10)))
# %%
sum(i for i in range(10))
# %%

def squared():
	for i in range(10):
		yield i**2

def negative(sequence):
	for el in sequence:
		yield -el

chained_generator = negative(squared())
# %%
next(chained_generator)
# %%
