# %% Array are contiguous data structures : They store information in adjoining blocks of memory. (by opposition to linked data structure which are chunks of memory linked by pointer, like linked-lists)

# %% lists are dynamic array : elements can be added or removed and python will automatically add or release memory
# You can hold different types together but the downside is that the data is less tightly packed => more memory needed
list((1,2,3)) # nice repr
# %%
# lists are mutable
a = [1, 2, 3]
a[1] = "fff"
print(a)
del a[1]
print(a)
# %%
# lists can hold arbitrary data type
[1,"44f", (1,2,3), [1,2], {4:4}]
# %% Tuples (immutable containers) : all elements must be defined at creation time
tup = 1,2,"three"
print(tup)
# %%
tup[1] = "rr"
# %%
del tup[2]
# %%
# adding element create copy of the tuple
tup + ("banzai",)
# %%
# Array from array module : only support one type (must be specified at creation)

import array
aa = array.array('d',[1,2])
print(aa)
aa[1] = "45"

# %%
# str
data = [12,25,31,42,54,67]
data2 = [0,0,0,0,0,0]
for i in range(len(data)):
        j = data[i]
        if j % 2:
            data2[i] = j
print(data2)

# %% str : immutable and recursive

mystr = "test"
print(type(mystr), type(mystr[1]))

# %%
mystr[1] ="e"
# %%
del mystr[2]
# %% unpacking
print(list(mystr))
# %%
print("/".join(list(mystr)))
# %%
# bytes : immutable sequences of single bytes (integer between 0 and 255)
# bytes are immutable but have a dedicated mutable type (bytearray)
arr = bytes((0,1,25,63))
print(arr[1])
# %% bytes have their own syntax
print(arr)

# %% range in 0 - 255
bytes((0,566))
# %%
arr[1] = 2
# %%
del arr[1]
# %% bytearray
arr2 = bytearray(arr)
arr2[1] = 5
# %%
# key takeaway : if you need to use array datastructures, start with a list or a tuple. If you have a very specific usecase, change the type then (it is often useful in the optimization part, not at first).
