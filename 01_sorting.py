# %% [markdown]
# # Sorting in python : https://docs.python.org/3/howto/sorting.html

# %%
import operator
a = [1, 3, 5, 4, 2, 5]
print(sorted(a))  # new list object
# lists also have a sort method :

# %%
print(a.sort())  # it returns none
# %%
print(a)  # sort method modified the list directly
# %%
sorted("Alpha, charlie, beta, Delta".split())

# %%
# The value of the key parameter should be a function (or other callable) that takes a single argument and returns a key to use for sorting purposes. This technique is fast because the key function is called exactly once for each input record.
sorted("Alpha, charlie, beta, Delta".split(), key=str.lower)
# %%
sorted([1, 5, 3, 10, 15, 19, 2, 5, 9, 13, 11, 2], key=lambda x: x > 6)


# %%
sorted([("John", 4), ("Mary", 2), ("Bob", 5), ("Karim", 1)], key=lambda x: x[1])

# %%
mydict = {"a": 4, "c": 2, "b": 3, "d": 1, "e": -8}
sorted(mydict.items())
# %%
sorted(mydict.items(), key=lambda x: x[1])
# %%
sorted(mydict.items(), key=operator.itemgetter(1))


# %%
class Sandwich:
    def __init__(self, ingredient, sauce, size):
        self.ingredient = ingredient
        self.sauce = sauce
        self.size = size

    def __repr__(self):
        return repr((self.ingredient, self.sauce, self.size))


sandwiches = [Sandwich("jambon", "ketchup", 50), Sandwich(
    "poulet", "mayonnaise", 100), Sandwich("tofu", "moutarde", 25),
	Sandwich("salad", "alsacienne", 25)]
print(sandwiches)
# %%
sorted(sandwiches, key=lambda x: x.size, reverse=True)

# %%
sorted(sandwiches, key=operator.attrgetter("size"))
# %%
sorted(sandwiches, key=lambda x: (x.size,x.sauce))

# %%
sorted(sandwiches, key=operator.attrgetter("size","sauce"))

# %%
# what if i want to organize by size and reverse by sauce ?
def multisort(xs, specs):
	for key, reverse in reversed(specs):
		xs.sort(key=operator.attrgetter(key), reverse=reverse)
	return xs

multisort(sandwiches, (("size", True), ("sauce", False)))
# %%
