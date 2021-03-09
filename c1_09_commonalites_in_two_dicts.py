# %% [markdown]
# # Commonalities in two dicts
# %%
# Reminder : sets
{1,2,{}} # elements in a set must be hashable
# Similarly to dict keys, elements in a set must be hashable. To see if an element exists in a set, first a hash lookup is performed and then the __eq__ method is used to see if elements should be considered equal
# In fact, because sets and dict keys are very similar, they share some methods
# %%
aa = set(("string1", 0,5,8, "string2"))
bb = {"string2", "string3", 0,6,9}
# %%
print(aa.intersection(bb))
print(aa & bb)
# %%
print(aa.union(bb))
print(aa | bb)

# %%
print(aa.difference(bb)) # in aa but not in bb
print(aa - bb)
# %%
print(aa.symmetric_difference(bb)) # in aa but not in bb
print(aa ^ bb)
print((aa | bb) - (aa & bb) == aa ^ bb)
# %% Application to dicts
a = {"x":1, "y":2, "z":3}
b = {"w":10, "x":11, "y":2}

print(a.keys() | b.keys()) # returns a set
# %%
print(a.keys().intersection(b.keys()))  # it seems the only set method is isdisjoint
# %%
a.items() & b.items() # returns a set of tuple of identical pairs
# %%
a.values() | b.values() # not implemented for values as they are not forced to be unique
# %%
set(a.values()) | set(b.values()) # workaround
# %%
# * filter 
d = {"xx":1, "yy":2, "zz":3, "tt":5}
e = {"xx":1, "yyy":2, "zzz":3, "tt":5}
{key:d[key] for key in d.keys() if key not in e.keys()}
# %%
{key:d[key] for key in d.keys() - e.keys()}
# %%

