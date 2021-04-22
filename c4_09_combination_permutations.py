#%%
"""
combinations
permutations
"""
#%%
import itertools

items = [1, 2, 3]

for p in itertools.permutations(items):
	print(p)
# %%
for p in itertools.permutations(items, r=2):
	print(p)
# %%
for p in itertools.permutations(items, 1):
	print(p)
# %%
for p in itertools.combinations(items, r=2):
	print(p)
# %%
for p in itertools.combinations_with_replacement(items, r=2):
	print(p)
# %%