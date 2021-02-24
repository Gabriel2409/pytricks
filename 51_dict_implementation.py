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
print(a == b, hash(a), hash(b))
print(a in [b], a is b)
# Just because two objects have the same hash does not mean they are identical !
# notice a in [b] returns True. With in, we only look at __eq__ : see EqNoHashClass
# %%


class HashNoEqClass:
    def __hash__(self):
        return 45

a = HashNoEqClass()
b = HashNoEqClass()
print(a == b, a is b, a in [b])
# having the same hash is not enough to be equal ! 
# %%


class EqNoHashClass:
    def __eq__(self, other):
        return True

a = EqNoHashClass()
b = EqNoHashClass()
print(a == b, a is b, a in [b]) # as expected, only __eq__ is used to test if a in [b]
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
# %% [markdown] What about dicts ? Time to focus ! 

crazy_dict = {True: "yes", 1: "no", 1.0: "maybe"}

# %%
crazy_dict
# ? What happened here ? 
#%% Let's decompose
decomposed_dict = dict()
decomposed_dict[True] = "yes"
print(decomposed_dict)
decomposed_dict[1] = "no"
print(decomposed_dict)
decomposed_dict[1.0] = "maybe"
print(decomposed_dict)
# ? So, can you guess ?

#%% 
# It seems we override the keys.
print(1 == 1.0)
print(True == 1)
print(isinstance(True, int)) # bools are subtypes of int !
# which means you can do that
print(["value0", "value1"][True]) # ! but seriously, don't


# %% Ok, I have to confess : in fact, to override a key in a dict, the __eq__ is not enough : in fact, python dicts are backed by a hash table data structure which allows for fast lookup. If two values have the same hash (which is a lot faster to calculate than to check for equality), then we look at the eq method to be sure that the key are identical. Indeed, sometimes, different keys have the same hash (it is called a hash collision)
# * ROMAN, I think we should rethink the way we define the hash method. It would allow for faster lookups in the prefill and would probably prevent the overriding of textboxes in our dict : we could do that witout losing all the functionalities given by our custom __eq__

class Test:
	def __init__(self, val, myhash,name):
		self.val = val
		self.hash = myhash
		self.name = name
	def __eq__(self, other):
		return self.val == other.val
	def __hash__(self):
		return self.hash
	def __repr__(self):
		return f"{self.name}<v={self.val},h={self.hash}>"

a = Test(0,0,"a")
b = Test(1,1,"b")
c = Test(0,0,"c")
d = Test(0,1,"d")
e = Test(1,0,"e")
print(a,b,c,d,e)
# %%
dct = {a:1, b:2,c:3, d:4, e:5}
print(dct)
# to overwrite a value : we need the same eq and same hash. Note that the key name is not changed (which makes sense because a and c are supposed to be identical as far as the dict is concerned)

# %% and what about our crazy dict ?
print(True == 1 == 1.0)
print(hash(True),hash(1),hash(1.0))
print(1 is 1, 1.0 is 1.0, True is True) 
print(1 is True, 1 is 1.0, 1.0 is True) # so a dict dont look at identity !

# %%

# %% [markdown]
# # Other types of dict
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
