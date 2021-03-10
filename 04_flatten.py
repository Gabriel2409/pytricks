# %%
from itertools import chain
# %%
aa = list(range(100))
bb = list(range(5,105))

#%%
%%timeit
[p for i in aa for p in bb]
[] # same as [item for sublist in list for item in sublist] but
# %%
%%timeit
list(chain.from_iterable(bb for i in aa))
# %%
%%timeit
a = []
for i in range(100):
	for p in range(i,i+100):
		a.append(p)
# %%
%%timeit
sum([bb for i in aa], [])

# %%
%%timeit
list(chain(*(bb for i in aa)))

# %%
