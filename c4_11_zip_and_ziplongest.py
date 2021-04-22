#%%
"""
zip: iterating over multiple sequences
zip longest
dict with zip
"""

xpoints = [1, 2, 3, 4, 5]
ypoints = [11, 12, 13, 14, 15]

for x, y in zip(xpoints, ypoints):
    print(x, y)

#%%
aa = zip(xpoints, ypoints)
aa
#%%
next(aa)

#%%
# zip creates an iterator, if you need a list 
list(zip(xpoints, ypoints))
#%%
zpoints = [101, 102, 103]
for x, z in zip(xpoints, zpoints):
    print(x, z)


# %%
from itertools import zip_longest

for x, z in zip_longest(xpoints, zpoints):
    print(x, z)
# %%


for x, z in zip_longest(xpoints, zpoints, fillvalue="<(^_^)>"):
    print(x, z)

# %%
mykeys = ["a", "b", "c"]
myvals = [1, 2, 3]

dict(zip(mykeys, myvals))

#%%
# final note :

for a, b, c in zip(range(3), range(4,7), range(8,11)):
	print(a,b,c)

# %%
