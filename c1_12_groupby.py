#%%
import operator
import itertools
rows = [
	{"price":15, "meal":"sandwich"},
	{"price":10, "meal":"pizza"},
	{"price":8, "meal":"sandwich"},
	{"price":7, "meal":"pizza"},
	{"price":9, "meal":"sandwich"},
	{"price":25, "meal":"salad"},
	{"price":32, "meal":"salad"},
	{"price":800, "meal":"chocolat cake with very good topping"},
]

sorted_rows = sorted(rows, key = operator.itemgetter("meal"))
# %%
for group, items in itertools.groupby(sorted_rows, key = operator.itemgetter("meal")):
	print(group)
	for item in items:
		print(item)
# %%
# you need to sort first
for group, items in itertools.groupby(rows, key = operator.itemgetter("meal")):
	print(group)
	for item in items:
		print(item)
# %%
