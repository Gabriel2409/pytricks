#%%
"""
slice of iterator
skip first part of iterator
"""
#%%
mylist = [0, 1, 2, 3, 4, 5, 6]
mylist[1:3]  # it works
# %%
iter(mylist)[1:3]  # does not work
# %%
def count():
    n = 0
    while True:
        yield n
        n += 1


# %%
mycount = count()
# %%
mycount[10:20]  # does not work either
# %%
import itertools

for element in itertools.islice(mycount, 10, 20):
    print(element)

# %%
next(mycount)  # huh It seems i consumed my iterator !
# %%
# * lets play with slicer. What happens if i iterate through my iterator and the slicer at the same time ?
mycount2 = count()
slicer = itertools.islice(mycount2, 10, 15, 2)
# %%
next(mycount2)
# %%
next(slicer)
# %%
"""
slicer consumed the iterator until it found the desired item (the one at index 10 in the remaining iterator); Then each time i call it, it looks at the current item in the iterator and adds 2. It keeps an internal count to stop at the right moment
"""
# %%
# * Skip first part of iterable

with open("fake_config.txt", "wt") as f:
    f.write("#\n")
    print("# fake comment", file=f)
    print("# another fake comment", file=f)
    print("beginning of the file", file=f)
    print("# comment in the file", file=f)
    print("middle of the file", file=f)
    print("end of the file", file=f)
# %%
with open("fake_config.txt", "rt") as f:
    for line in itertools.dropwhile(lambda line: line.startswith("#"), f):
        print(line, end="")

# %%

from functools import wraps
import inspect


def optional_debug(func):

    # prevents debug from being an arg of the function
    if "debug" in inspect.getfullargspec(func).args:
        raise TypeError("Debug arg already defined")

    @wraps(func)
    def wrapper(*args, debug=False, **kwargs):
        if debug:
            # do debug stuff
            print("Calling", func.__name__)
        return func(*args, **kwargs)

    # modifies signature so that it adds debug arg to the func
    sig = inspect.signature(func)
    parms = list(sig.parameters.values())
    parms.append(
        inspect.Parameter("debug", inspect.Parameter.KEYWORD_ONLY, default=False)
    )
    wrapper.__signature__ = sig.replace(parameters=parms)
    return wrapper


# %%
@optional_debug
def passer():
    pass

passer.__signature__
# %%

# %%
