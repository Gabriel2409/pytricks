#%% [markdown]
# min, max and sorted on a dict

prices = {"Alpha": 5, "Charlie": 2, "Bravo": 7}

print (min(prices))
print(sorted(prices))
# problems : it only looks at the keys
# %%
print(min(prices.values()))
print(sorted(prices.values()))
# %%
# order by values ? 
print(sorted(prices.items(), key = lambda x:x[1])) # lambda x: (x[1], x[0])
print(min(prices.items(), key = lambda x:x[1]))
# %%
import operator
print(sorted(prices.items(), key=operator.itemgetter(1,0))) 

# %%
print(dict(sorted(prices.items(), key = lambda x:x[1]))) # i can even show it as a dict but keep in mind that you shouldn't rely on the order of the keys in the dict (use OrderedDict)
# %%
# another way is to invert values and keys and create a zip object. When i call min or sorted it first looks at the first element of the tuple (the value) and then at the second (the key). 
print(sorted(zip(prices.values(), prices.keys())))
# %%
