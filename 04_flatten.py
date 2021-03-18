# %% [markdown]
# # flatten a list
"""
all the ways to flatten a list
Spoiler : use chain if you want to go fast
"""
# %%
# # experiments
from itertools import chain

# %%
def create_sublist(i, max_val):
	sub = []
	for j in range(max_val):
		sub.append(f"s{i}_{j:03d}")
	return sub

# %%
mysmalllist = [create_sublist(i,3) for i in range(3)]
# %%
"""
All the methods below give the same result
"""
# %%
[item for sublist in mysmalllist for item in sublist]
# %%
sum([sublist for sublist in mysmalllist], [])
# %%
list(chain(*(sublist for sublist in mysmalllist)))
# %%
list(chain.from_iterable(sublist for sublist in mysmalllist))
# %%
"""
Timing
"""
# %%
nb_elem_per_sublist = 100
nb_sublists = 100
mylist = [create_sublist(i,nb_elem_per_sublist) for i in range(nb_sublists)]
# %%
%%timeit
[item for sublist in mylist for item in sublist] # almost as fast as chain if nb of sublist is small
# %%
%%timeit
sum([sublist for sublist in mylist], [])
# %%
%%timeit
list(chain(*(sublist for sublist in mylist)))
# %%
%%timeit
list(chain.from_iterable(sublist for sublist in mylist))
# %%
