#%% remove duplicate 
# hashable types

def dedupe(items):
	seen = set()
	for item in items:
		if item not in seen:
			yield item
			seen.add(item)

print(list(dedupe([1,2,3,4,5,4,5,4,5,4,3,5,2,10])))

# %%
list(dedupe([{"a":1}, {"a":1}, {"a":2}])) # not good
# %%
def dedupe(items, key=None):
	seen = set()
	for item in items:
		val = item if key is None else key(item)
		if val not in seen:
			yield item
			seen.add(val)
# %%
list(dedupe([{"a":1}, {"a":1}, {"a":2}], key = lambda x: x["a"]))

# %%
tboxlist = []
textboxes = ["tbox1", "tbox2", "tbox3", "tbox4", "tbox4", "tbox1", "tbox6"]
for tbox in dedupe(textboxes):
	tboxlist.append(tbox)
print(tboxlist)

# %%
for i in set([1,2,0]):
	print(i)
# %%
