#%% Intro
"""
Decorator : naive vs wraps
update_wrapper / wraps implementation
access wrapped element
stack decorators
"""
#%% 

def gothrough(n):
    """Goes through n number"""
    for _ in range(n):
        pass

gothrough(1000)
# %%
import time
def timethis(func):
    """Times a func (naive approach)"""
    def wrapper(*args, **kwargs):
        """wrapper docstring"""
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print(f"Elapsed time: {end - start:.2f}s")
    return wrapper

timethis(gothrough)(10000000)

# %%

@timethis
def gothroughagain(n):
    """Goes through n number again !"""
    for _ in range(n):
        pass

gothroughagain(10000000) # a decorator at function definition is the same thing as calling the function inside the wrapper !
# %% However, there is a problem with our approach

print(timethis.__doc__)
print(gothrough.__doc__)
# %%
print(gothroughagain.__doc__) 
# Huh i probably dont want to see the wrapper docstrings ! Note that usually you dont put docstrings in the wrapper, it was just for the example
# %% A better way to create a decorator
from functools import wraps, update_wrapper
# the wraps decorator calls the update_wrapper function from the functools module. 
# It updates lots of attributes from the wrapped function to the wrapper function, such as __doc__

def timethisbetter(func):
    """Times a func with wraps decorator"""
    def wrapper(*args, **kwargs):
        """wrapper docstring"""
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print(f"Elapsed time: {end - start:.2f}s")
    wrapper = update_wrapper(wrapper, wrapped=func)
    return wrapper

@timethisbetter
def gothroughoncemore(n):
    """Goes through n number once more"""
    for _ in range(n):
        pass

print(gothroughoncemore.__doc__)
# %% In fact, there is a decorator in functools that calls update wrapper
def timethisbest(func):
    """Times a func with wraps decorator"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        """wrapper docstring"""
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print(f"Elapsed time: {end - start:.2f}s")
    return wrapper

@timethisbest
def gothroughlasttime(n):
    """Goes through n number for the last time"""
    for _ in range(n):
        pass

print(gothroughlasttime.__doc__)
# %%
# ! AND SO YOU HAVE IT : ALWAYS USE THIS FORMAT FOR YOUR DECORATOR AND YOU WONT HAVE A HEADACHE
gothroughlasttime(50)
# %% [markdown]
# * ok, I probably went a bit fast from update_wrapper to @wraps(func)
# lets look at the source code of wraps
# https://github.com/python/cpython/blob/master/Lib/functools.py

"""
def wraps(wrapped,
          assigned = WRAPPER_ASSIGNMENTS,
          updated = WRAPPER_UPDATES):

    return partial(update_wrapper, wrapped=wrapped,
                   assigned=assigned, updated=updated)
"""
# partial ? 
from functools import partial
def f1(a,b):
    return a+b

def f2(b):
    return partial(f1, b=b)
print(f2(5))
print(f2(5)(a=7))

"""
which means these three implementations are equivalent and this is why we use @wraps(func)

@wraps(func)
def wrapper(*args, **kwargs):
    func(*args, **kwargs)
    ...

def wrapper(*args, **kwargs):
    func(*args, **kwargs)
    ...
    wrapper = wraps(func)(wrapper)

def wrapper(*args, **kwargs):
    func(*args, **kwargs)
    ...
    wrapper = update_wrapper(wrapper, wrapped=func)
    """

#%%
# * ok, what about update_wrapper then ? 
"""
WRAPPER_ASSIGNMENTS = ('__module__', '__name__', '__qualname__', '__doc__',
                       '__annotations__')
WRAPPER_UPDATES = ('__dict__',)
def update_wrapper(wrapper,
                   wrapped,
                   assigned = WRAPPER_ASSIGNMENTS,
                   updated = WRAPPER_UPDATES):
    for attr in assigned:
        try:
            value = getattr(wrapped, attr)
        except AttributeError:
            pass
        else:
            setattr(wrapper, attr, value)
    for attr in updated:
        getattr(wrapper, attr).update(getattr(wrapped, attr, {}))
    # Issue #17482: set __wrapped__ last so we don't inadvertently copy it
    # from the wrapped function when updating __dict__
    wrapper.__wrapped__ = wrapped
    # Return the wrapper so this can be used as a decorator via partial()
    return wrapper
"""

#* So what it means is : the attributes __module__, __name__, __qualname__, __doc__, __annotations__ are transferred from the decorated function to the wrapper
# * the __dict__ of the wrapper is updated with the __dict__ of the decorated func
# * the __wrapped__ attribute is set to point to the decorated func

# %%
# Unwrapping
# you can access the function without the decorator
gothroughlasttime.__wrapped__(88) # nothing is printed
# %%
# Remember our first implementation ?
gothrough.__wrapped__(88) # it does not work
# %%
# * Let's decorate a function multiple times

def timer(func):
    """Times a func with wraps decorator"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print(f"Elapsed time: {end - start:.2f}s")
    return wrapper


def printname(func):
    """Times a func with wraps decorator"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("func_name", func.__name__)
        func(*args, **kwargs)
    return wrapper

@timer
@printname
def myfunc():
    for _ in range(1000000):
        pass
    print("done")

myfunc()

# same as myfunc = timer(printname(myfunc))
# %%
myfunc.__wrapped__() # what will i get ?
# %%
myfunc.__wrapped__.__wrapped__()

"""The way it is implemented in the source code : for each stacked decorator, the __wrapped__ attribute of the wrapper points directly to the function it wraps"""
# %%
import inspect
# it seems inspect follows the wrapped chain to return the original function.
# More analysis on the inspect module would be nice
inspect.unwrap(myfunc)()
# %%
"""
Further investigation shows that in python 3.5, the @wraps appears to preserve signature but does have issues. Some developers created other packages to really preserve the signature. More work to understand signature is needed to see if functools.wraps actually does what it is supposed to do or if there are obscure cases where it does not work.
I dont know if the issue exists in new versions of python

On a first approach, i think that we should probably do as if it works, because it is what is widely used but maybe we can have unexpected issues with decorators
https://stackoverflow.com/questions/308999/what-does-functools-wraps-do/55102697#55102697
"""

# %%
inspect.signature(myfunc)
# %%
inspect.signature(myfunc, follow_wrapped=False)

# %%
