#%%
"""
change with slice

"""
#%%
mylist = [0, 1, 2, 3, 4]

mylist[0:2] = ["a", "b"]
print(mylist)
# %%
mylist = [0, 1, 2, 3, 4]

mylist[0:2] = ["a"]
print(mylist)
# %%
mylist = [0, 1, 2, 3, 4]

mylist[0:2] = ["a", "b", "c"]
print(mylist)

# %%
# inserts before
mylist = [0, 1, 2, 3, 4]
mylist.insert(1, 'a')
print(mylist)
# %%
# if insert number is greater than length, appends
mylist = [0, 1, 2, 3, 4]
mylist.insert(454554444, 'a')
print(mylist)
# %%
%%timeit
mylist = list(range(10000000))
mylist.insert(5, 'a')
# %%
%%timeit
mylist = list(range(10000000))
mylist.append('a')
# %%
# append and insert at the end take the same time in lists. However insert at beginning is O(n). More details in stack.py
# %%
mylist = ["a","b","c","d"]
print(mylist.pop(2)) # returns (the popped value)
print(mylist)
# %%
mylist.pop() # by default, pops the last element
# %%
mylist.pop(545454) # unlike insert, index error
# %%
