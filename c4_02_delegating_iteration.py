#%%
"""
delegating iteration from container to inner items
yield in __iter__
"""
# %%
# in the iterator protocol, __iter__ usually returns self. However, you can also point to an attribute


class MyListWithMetaData:
    def __init__(self, mylist, metadata):
        self.mylist = mylist
        self.metadata = metadata

    def __iter__(self):
        return self.mylist.__iter__()

aa = MyListWithMetaData([1,2,3], "extrainfo")
# %%
for el in aa:
    print(el)
# %%
# * Because the __iter__ forwards the iteration to the inner list, no need to define a __next__. Indeed it would never be called here as the next that is called is the one of the list. Proof below

class MyListContainer1:
    def __init__(self, mylist):
        self.mylist = mylist
        self.current_index = 0

    def __iter__(self):
        print("__iter__ is called")
        return self

    def __next__(self):
        print("__next__ is called")
        current_index = self.current_index
        try:
            val = self.mylist[current_index]
            self.current_index +=1
            return val
        except IndexError:
            raise StopIteration
# %%
for el in MyListContainer1([1,2,3]):
    print(el) # ? What will be printed ? 
# %%
class MyListContainer2:
    def __init__(self, mylist):
        self.mylist = mylist

    def __iter__(self):
        print("__iter__ is called")
        return self.mylist.__iter__()

    def __next__(self):
        print("__next__ is called")
        raise ValueError("Should not be accessed")
# %%
for el in MyListContainer2([1,2,3]):
    print(el) # ? What will be printed ? 
# %%
# ! Note : you can implement __iter__ as a generator if you dont want to use next
class MyListContainer3:
    def __init__(self, mylist):
        self.mylist = mylist

    def __iter__(self):
        print("__iter__ is called")
        for el in self.mylist:
            yield el

for el in MyListContainer3([1,2,3]):
    print(el) # ? What will be printed ? 
# %%
