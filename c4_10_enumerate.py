#%%

mylist = ["a", "b", "c"]

for i in range(len(mylist)):
    print(i, mylist[i])
#%%
i = 0
for el in mylist:
    print(i, el)
    i += 1

# %%
# better way
for idx, el in enumerate(mylist):
    print(idx, el)
#%%
# note that you can start enumeration at another number
for idx, el in enumerate(mylist, 5):
    print(idx, el)
#%%
# What is enumerate ?

aa = enumerate(mylist)

# %%
next(aa)
#%%
# be careful with tuples
mylist2 = [("a", "b",), ("c", "d")]

for idx, x, y in enumerate(mylist2):
    print(idx, x, y)
# ? error ? 



#%%


for idx, (x,y) in enumerate(mylist2):
	print(idx, x,y )
# %%

