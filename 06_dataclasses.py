#%%
"""
Tedious work with classes
Improvement with dataclasses
Small tricks with dataclasses
"""
#%%
import inspect
import functools

#%%

# * Let's say I want to create a class called item containing two fields :
# * the price and the name


class Item:
    # I need an init
    def __init__(self, price: float, name: int):
        self.price = price
        self.name = name

    # remember, i also need a repr
    def __repr__(self):
        return f"{self.__class__.__name__}(price={self.price}, name={self.name})"


# %%
i = Item(45, "pizza")
print(i)
# %%
# * ok great, but what if I need to compare items ?
class Item:
    def __init__(self, price: float, name: int):
        self.price = price
        self.name = name

    def __repr__(self):
        return f"{self.__class__.__name__}(price={self.price}, name={self.name})"

    def __eq__(self, other):
        if isinstance(other, Item):
            if self.price == other.price and self.name == other.name:
                return True
        return False


# %%
print(Item(45, "pizza") == Item(45, "pizza"))
print(Item(45, "pizza") == Item(46, "pizza"))
print(Item(45, "pizza") == (46, "pizza"))
# %%
print(Item(45, "pizza") < Item(45, "pizza"))

# %%
# ** Huh, so now, if I want to compare Items, I need other functions.
class Item:
    def __init__(self, price: float, name: int):
        self.price = price
        self.name = name

    def __repr__(self):
        return f"{self.__class__.__name__}(price={self.price}, name={self.name})"

    def __eq__(self, other):
        if isinstance(other, Item):
            if self.price == other.price and self.name == other.name:
                return True
        return False

    def __lt__(self, other):
        if isinstance(other, Item):
            return (self.price, self.name) < (other.price, other.name)
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Item):
            return (self.price, self.name) <= (other.price, other.name)
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Item):
            return (self.price, self.name) > (other.price, other.name)
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Item):
            return (self.price, self.name) >= (other.price, other.name)
        return NotImplemented


print(Item(45, "pizza") <= Item(45, "pizza"))
print(Item(44, "wasabi") > Item(45, "pizza"))
print(Item(45, "wasabi") > Item(45, "pizza"))

# %%
inspect.getmembers(Item, inspect.isfunction)  # user defined functions
# %%
# * That was tedious. Note that i can use total_ordering from functools to speed up the process
@functools.total_ordering
class Item:
    def __init__(self, price: float, name: int):
        self.price = price
        self.name = name

    def __repr__(self):
        return f"{self.__class__.__name__}(price={self.price}, name={self.name})"

    def __eq__(self, other):
        if isinstance(other, Item):
            if self.price == other.price and self.name == other.name:
                return True
        return False

    def __lt__(self, other):
        if isinstance(other, Item):
            return (self.price, self.name) < (other.price, other.name)
        return NotImplemented


print(Item(45, "pizza") > Item(49, "pizza"))

inspect.getmembers(Item, inspect.isfunction)  # user defined functions

#%%
# * ok great, what if I want to make the item hashable to use in a dictionary ?
# * a good practice is to make the properties immutables. I can mimick this
# * behavior by adding property.
@functools.total_ordering
class Item:
    def __init__(self, price: float, name: int):
        self._price = price
        self._name = name

    @property
    def price(self):
        return self._price

    @property
    def name(self):
        return self._name

    def __hash__(self):
        return hash((self.__class__, self.price, self.name))

    def __repr__(self):
        return f"{self.__class__.__name__}(price={self.price}, name={self.name})"

    def __eq__(self, other):
        if isinstance(other, Item):
            if self.price == other.price and self.name == other.name:
                return True
        return False

    def __lt__(self, other):
        if isinstance(other, Item):
            return (self.price, self.name) < (other.price, other.name)
        return NotImplemented


#%%
i = Item(45, "sandwich")
j = Item(48, "pizza")
i.price = 49
# %%
{i: "first", j: "second"}
# %%
# * SUMMARY
# * Perfect, we created a class with two fields that:
# * 1. is correctly initialized
# * 2. Has a correct repr
# * 3. Can support ordering (same as comparing the class as tuples)
# * 4. Can support hash (in this case, it is immutable
# * provided you dont access the private attributes)
# ! BUT.....
# ! I realized I forgot to add the nb of calories !
# * => I need to modify __init__, __eq__, __lt__, __hash__, __repr__,
# * and I need to add another property
# %%
"""dataclass to the rescue"""
from dataclasses import dataclass


@dataclass
class Item:
    price: float
    name: str


# %%
inspect.getmembers(Item, inspect.isfunction)
print(Item(45, "pizza"))
print(Item(45, "pizza") == Item(45, "pizza"))
print(Item(45, "pizza") == (45, "pizza"))
print(Item(46, "pizza") == Item(45, "pizza"))
# %%
print(Item(45, "pizza") < Item(45, "pizza"))
# %%
# * with ordering
@dataclass(order=True)
class Item:
    price: float
    name: str


print(Item(45, "pizza") <= Item(45, "pizza"))
print(Item(45, "pizza") > Item(44, "pizza"))
print(Item(45, "apple") > Item(45, "banana"))
inspect.getmembers(Item, inspect.isfunction)
# %%
# * with hash and immutability
@dataclass(frozen=True)
class Item:
    price: float
    name: str


i = Item(45, "pizza")
j = Item(46, "apple")
# %%
i.price = 49
# %%
{i: "first", j: "second"}
# %%
inspect.getmembers(Item, inspect.isfunction)

# %%
# * In fact, you can pass a lot of arguments to dataclass.
# * If you dont pass any, you get the default
"""@dataclass(init=True, 
    repr=True,
    eq=True,
    order=False,
    unsafe_hash=False,
    frozen=False
    )
"""
#%%
# * lets rewrite the example with hash and ordering with dataclasses


@dataclass(order=True, frozen=True)
class Item:
    price: float
    name: str


inspect.getmembers(Item, inspect.isfunction)

# %%
"""small tricks"""
# Now, what if you want to do a cool stuff in init.
