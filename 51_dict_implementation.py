# %%
from collections import OrderedDict, defaultdict
my_dict = {'key1': "value1", "key2": 9, 45: "ff", (45, 78): 39}
print(my_dict)
print(dict(a=1, b=2))
# %% methods
my_dict = {"a":1, "b":2}
my_dict.clear()
print(my_dict)
print(dict.fromkeys(['a', 'b']))
print(dict.fromkeys('ab'))
#%%
aa = dict.fromkeys('abc')
print(aa.pop("b")) # pop returns none 
print(aa) # but modified dict

#%%
aa = dict.fromkeys('abc')
print(aa.popitem()) # popitem pops last inserted element
print(aa) # but modified dict
#%%
aa = dict.fromkeys('abc')
aa.setdefault("e","BOOM")
print(aa["e"])

aa = dict.fromkeys('abcde')
aa.setdefault("e","BOOM")
print(aa["e"])
#%%
aa = {"a":1}
aa.update({"b":2})
print(aa)
aa.update({"b":3})
print(aa)
#%%
print(aa.get('a'))
print(aa.get('w'))
print(aa.get('w',[]))
#%%
for key, val in aa.items():
	print(key,val)
for key in aa.keys():
	print(key)
for val in aa.values():
	print(val)
# %%
print({x: x**2 for x in range(3)})
# %%
my_not_working_dict = {[45, 45]: 45}

# %% Python dicts are indexed by keys that can be of any hashable type. A hashable object has a hash value that never changes during its lifetime and it can be compared to other objects. In addition two hashable objects that compare as equal must have the same hash value

print(1 == 1, 1 is 1)
print("aa" == "aa", "aa" is "aa")
print((1, 2) == (1, 2), (1, 2) is (1, 2))
print([1, 2] == [1, 2], [1, 2] is [1, 2])
print({1: 2} == {1: 2}, {1: 2} is {1: 2})

# %%
print(hash(1), hash("aa"), hash(((1, 2))), hash(((1, 2))))
# %%

print(hash([1, 2]))
# %%
# list has an __eq__ method but not a hash method
# %%
# let's build a class where the equality comparison always return true and the hash is constant


class HashAndEqClass:
    def __hash__(self):
        return 45

    def __eq__(self, other):
        return True


a = HashAndEqClass()
b = HashAndEqClass()
print(a == b)
print(hash(a), hash(b))
print(a is b)
# Just because two objects have the same hash does not mean they are identical !
# %%


class HashNoEqClass:
    def __hash__(self):
        return 45


a = HashNoEqClass()
b = HashNoEqClass()
print(a == b)
print(a is b)
# %%


class EqNoHashClass:
    def __eq__(self, other):
        return True


a = EqNoHashClass()
b = EqNoHashClass()
print(a == b)
print(a is b)
# %%
print(hash(a))
# %%
# A good practice when you want to define an __eq__ is to define a __hash__ too.
a = HashAndEqClass()
print({a: 5})
# %%
a = HashNoEqClass()
print({a: 5})
# %%
a = EqNoHashClass()
print({a: 5})


# %%
# Conclusion 1 : if you want to use an object as a key in a dict, it must be hashable

# %% bonus hash of strings are salted
hash("rrrr")
# %%
# if key order is important for your algorithm to work, use OrderedDict
print(OrderedDict(key1='value1', key2=2, key3="rrr"))

# %%
print(OrderedDict({"key1": 'value1', "key2": 2, "key3": "rrr"}))
# %%

orddict = OrderedDict({ f"key_{x}":f"value_{x}" for x in range(10)})
print(orddict)



# %%
orddict.popitem(last=True) # last defaults to True
# %%
orddict.popitem(last=False)
# %%
print(orddict)
# %%
orddict.move_to_end("key_3", last=True)
print(orddict)
# %%
orddict.move_to_end("key_3", last=False)
print(orddict)
# %%
# Note : a way to pretty print
import json
print(json.dumps(orddict,indent=4))
# %%
aa = [1,2,3,4]
[a for a in reversed(aa)]

# %%
for key, val in reversed(orddict.items()):
	print(key,val)

# %%
# Note that when creating a class, you can define a __reversed__ method
class OrderedLetters:
	def __init__(self, list_of_letters):
		self.ordered_list =  sorted(list_of_letters)
	def __repr__(self):
		return str(self.ordered_list)
	def __reversed__(self):
		return iter(sorted(self.ordered_list, reverse=True))

OrderedLetters(['a', 'c', 'b'])
# %%

for l in reversed(OrderedLetters(['a', 'c', 'b'])):
	print(l)
# %%

# %%

dd = defaultdict(int, {"a":1})
print(dd["a"])
print(dd.get("b")) # ! can be a problem
print(dd["b"])
print(dd.get("b")) # ! works as expected 
print(dd.get("b",5)) # does not work

# %%

class MyDict(dict):
	def __missing__(self, key): # methods for subclasses of dicts
		print("calling __missing__ method")
		rv = []
		return rv

m = MyDict()
m["a"]=1
print(m)
print(m["b"])
print(m)

# %%
df = defaultdict(lambda : "<miss>", {"a":1})
df["fa"]
# %%
df = defaultdict(set, {"a":1})
print(df["fa"])
print(df.get("fa",5))
# %%
# * Chain maps
from collections import ChainMap
dict1 = {'a':1, 'b':2, 'c':3}
dict2 = {'c':4, 'd':5, 'e':6}
dict3 = {'a':7, 'c':9, 'w':15}
# %%
chain = ChainMap(dict1, dict2, dict3)
print(chain)
# %%
print(chain["a"], chain["d"], chain["w"])
# %%
print(chain["ffw"])
# %%
chain.maps # returns a list of dictionnary in order

# %%
new_chain = chain.new_child({"AA":11})
print(new_chain)
# %%
ChainMap({"BB":4545},*chain.maps)
# %%
chain.parents

# %%
# same as 
ChainMap(*chain.maps[1:])

# %%
chain, list(chain.items()) # for iteration maps are scanned last to first
# %% why use chainmaps ?
# You can keep defaults with no need to overwrite
default_values= {"prefill_tsi": ["AmountTextBox"], "prefill_country": ["CountryNameTextBox"],}
special_use_case = {"prefill_tsi": ["AmountTextBox", "PercentageTextBox"]}

chain = ChainMap(special_use_case, default_values)

chain["prefill_tsi"], chain["prefill_country"]

# %%
# * wrapper to make read only dicts: MappingProxyType : useful to protect state for ex : no need to create a full copy of the dict
from types import MappingProxyType
writable = {"a":1,"b":2}
# %%
read_only = MappingProxyType(writable)
writable, read_only

# %%
read_only["d"] = 5
# %%
# updates to the original are reflected in the proxy
writable["c"] = 5
writable, read_only
# ! In conclusion, dict are the central data structure in python. Most of the time the standard implementation is enough. Use orderedDict to communicate the intent that order is important. Use defaultdict when you find yourself trying to access keys that may or may not be defined.