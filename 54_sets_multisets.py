#%%
# a set is an unordered collection of objects that dont allow duplicates
# sets are used to quickly test a value for membership in the test, to insert or delete new values from a set and to compute the union or intersection of two sets;
# membership tests are O(1). Union and intersection are O(n)
example_set = {"a", "b"}
"b" in example_set
# %%
empty_set = set()

# %% lookup is faster than a list
l = list(range(100000))
s = set(range(100000))
# %%
%%timeit
"a" in l # 1.16ms
# %%
%%timeit
"a" in s # 46.3 ns
# %%
%%timeit
"a" in set(l) #2.53 ms : building a set and searching in it is still longer

# %%
s2 = {1,2}
s2.add(3)
s2.remove(2)
print(s2)
# %%
a = {1,2,3,4}
b = {3,4,5,6}
c = {3,4,5,6}
print(a.union(b), a.intersection(b))
print(a == b, b == c)
# %%
{a:4} # sets are not hashable
# %%
vowels = frozenset({"a","e","i","o","u"})

# %%
vowels.remove("a")
# %%
vowels.add("4a")

# %%
{vowels:4} # frozen sets are hashable and can be used as dict keys
# %%
hash(vowels)
# %%
vowels == set(vowels) # the __eq__ does not check if set is frozen or not
# %%
from collections import Counter
isinstance(Counter(), dict)
# %%
# counter is a dict but can be seen as a set where we allow multiple occurence of an element.
print(Counter(["a","a","a","b","c","c"])) # counts occurences in an iterable
print(Counter({"a":5, "b":1})) # transforms dict in counter
# %%
bb = Counter()
bb.update({"a":5, "b":6})
bb.update("a") # update with a dict key (can also create another key)
print(bb)
bb.update(["a","a","b","c"])
print(bb)
bb.update({"a":-1})
print(bb)
bb.subtract("b")
print(bb)
bb.subtract({"f":5})
print(bb)
# %%
print(sorted(bb.elements()))
print(bb.most_common(2))

# %%
print(len(bb)) # same as bb.keys() : nb of different keus
print(sum(bb.values())) # sum of all the values == nb of occurences if all values are positive ! Note that you should always have positive values in a counter. It is not enforced but that is the way they are supposed to be used
# %% be careful when you transform a dict
aa = Counter({"a":"ff"})
print(aa)
aa.update({"a":1})
print(aa)
# %%
aa.update({"a":"1"})
print(aa)
# %%
# ! The Counter class itself is a dictionary subclass with no restrictions on its keys and values. The values are intended to be numbers representing counts, but you could store anything in the value field : you will probably use it a lot in nlp problems. It is very useful to count the occurence of words in a text
# The most_common() method requires only that the values be orderable.
# For in-place operations such as c[key] += 1, the value type need only support addition and subtraction. So fractions, floats, and decimals would work and negative values are supported. The same is also true for update() and subtract() which allow negative and zero values for both inputs and outputs.
# The multiset methods are designed only for use cases with positive values. The inputs may be negative or zero, but only outputs with positive values are created. There are no type restrictions, but the value type needs to support addition, subtraction, and comparison.
# The elements() method requires integer counts. It ignores zero and negative counts.
