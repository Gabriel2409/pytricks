# %%
my_dict = {'key1': "value1", "key2": 9, 45: "ff", (45,78):39}
print(my_dict)

# %%
print({x:x**2 for x in range(3)})
# %%
my_not_working_dict = {[45,45]:45}

# %% Python dicts are indexed by keys that can be of any hashable type. A hashable object has a hash value that never changes during its lifetime and it can be compared to other objects. In addition two hashable objects that compare as equal must have the same hash value

print(1 == 1, 1 is 1)
print("aa" == "aa", "aa" is "aa")
print((1,2) == (1,2), (1,2) is (1,2))
print([1,2] == [1,2], [1,2] is [1,2])
print({1:2} == {1:2}, {1:2} is {1:2})

# %%
print(hash(1), hash("aa"), hash(((1,2))), hash(((1,2))))
# %%

print(hash([1,2]))
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
print(a==b)
print(hash(a), hash(b))
print(a is b)
# Just because two objects have the same hash does not mean they are identical ! 
# %%
class HashNoEqClass:
	def __hash__(self):
		return 45

a = HashNoEqClass()
b = HashNoEqClass()
print(a==b)
print(a is b)
# %%
class EqNoHashClass:
	def __eq__(self, other):
		return True
a = EqNoHashClass()
b = EqNoHashClass()
print(a==b)
print(a is b)
# %%
print(hash(a))
# %%
# A good practice when you want to define an __eq__ is to define a __hash__ too.
a = HashAndEqClass()
print({a:5})
# %%
a = HashNoEqClass()
print({a:5})
# %%
a = EqNoHashClass()
print({a:5})


# %%
# Conclusion 1 : if you want to use an object as a key in a dict, it must be hashable

# %% bonus hash of strings are salted
hash("rrrr")
# %%
# if key order is important for your algorithm to work, use OrderedDict
from collections import OrderedDict
print(OrderedDict(one=1, two=2))
# %%
