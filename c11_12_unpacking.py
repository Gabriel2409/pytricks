#%% [markdown]
"""
Unpacking into separate variables
Positional and keyword only args in functions
Unpacking in functions
"""

# # 1.1 Unpacking a sequence into separate variables
p = (57, "test")
a, b = p
print(a)
print(b)
# %%
p2 = [1, 2, 3, 4]
a, b, c, d = p2
print(a)
print(b)
print(c)
print(d)
# %%
# Unpacking works with any object that is an iterable
mydict = {"a": 1, "b": 2}
d1, d2 = mydict
print(d1)
print(d2)
# %%
a, b, c, d, e = "Hello"
print(b)
# %%
a, b = (i for i in range(2))  # generator
print(a)
# %%
a, b, c = range(3)  # range
print(b)
# %%
a, b = zip(range(2), range(2, 4))  # zip objects
print(b)
# %%
# Discard values you don't need with _
data = ["Important", "Not important", "Very Important", "Not important either"]
a, _, c, _ = data
print(a)
print(c)
print(_)  # note that it still stored the var
# %%
#%% [markdown]
# # 1.2 Unpacking elements from iterables of arbitrary length
# You may have noticed an issue if we don't know the number of items in the iterable
a, b = range(3)
# %%
a, b, c = range(2)
# %%
# Pb : you know your data looks like this [first, middle1, middle2, ..., middlen, last] and you want to unpack all the middle in a list
a, b, c = ["first", "middle1", "last"]
print(a)
print(b)
print(c)
# %%
a, b, c = ["first", "middle1", "middle2", "last"]
# %%
# You could do
a, b1, b2, c = ["first", "middle1", "middle2", "last"]
b = [b1, b2]
# but what if you don't know the number of elements in the middle ?
# %%
a, *b, c = ["first", "middle1", "middle2", "last"]
print(a)
print(b)
print(c)
# %%
a, *b, c = ["first", "middle1", "middle2", "middle3", "last"]
print(b)
# %% if you dont care about the middle
a, *_, c = ["first", "middle1", "middle2", "middle3", "last"]
print(a,c)
# %%
a, *b, c = ["first", "last"]
print(b)  # we always get a list
# %%
# ! only one unpack allowed in a list
a, *b, *c, d = ["first", "middle1", "middle2", "middle3", "last"]
# %%
# unpacking can be very useful when iterating through tuples of variable length
records = [("age", 25), ("address", "Paris", "France"), ("age", 26)]


def show_age(number):
    print(f"Your age is {number:d}")


def show_address(city, country):
    print(f"You live in {city:s} ({country:s})")


for tag, *args in records:
    if tag == "age":
        show_age(*args)
    elif tag == "address":
        show_address(*args)
# %% # Here I showed you how to unpack args in a function.
# Note that you can unpack keyword args too


def keyword_func(*, name: str, age: int, country: str):
    print(
        f"You are {age:d} years old. Your name is {name:s} and you live in {country:s}"
    )


# %%
keyword_func("Jon", 25, "America")
# %%
keyword_func(name="Jon", age=25, country="America")

# %%
my_dict_info = {"name": "Karol", "country": "Norway", "age": 46}
keyword_func(**my_dict_info)

# %% Note


def positional_func(food: str, price: int, /):
    print(f"You ordered a {food:s} for {price:d}€")


# %%
positional_func("burger", 5)
# %%
positional_func(food="burger", price=5)
# %%
food_and_price = ("pizza", 8)
positional_func(*food_and_price)

# %% Combine
def positional_and_keyword_func(
    food: str, price: int, /, *, name: str, age: int, country: str
):
    print(
        f"You are {age:d} years old. Your name is {name:s} and you live in {country:s}. You ordered a {food:s} for {price:d}€"
    )

food_and_price = ("ice cream", 4)
my_dict_info = {"name": "Jack", "country": "Denmark", "age": 19}

positional_and_keyword_func(*food_and_price, **my_dict_info)
# %%
