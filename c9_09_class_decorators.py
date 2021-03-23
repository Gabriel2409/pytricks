#%%
""" 
class decorator : basic
class decorator : __get__
"""

#%% [markdown]
# # Class decorators for functions
#%%
import types
from functools import wraps

class Profiled:
    def __init__(self, func):
        wraps(func)(self)
        self.ncalls = 0

    def __call__(self, *args, **kwargs):
        self.ncalls += 1
        print("CALL", self.ncalls)
        return self.__wrapped__(*args, **kwargs)


@Profiled
def printcolor(color="blue"):
    print(color)
# %%
printcolor("blue")
# %%
# remember all the stuff with nonlocal ? No need here, it works because ncalls is an attribute of our class
printcolor.ncalls = 0
printcolor("red")
# %%
printcolor.__call__("green")
# %% lets look into more details
isinstance(printcolor, Profiled)
# %% so the decorator transformed my func into an instance of Profiled
# the first line in __init__ sets the correct metadata for the instance
# then  __call__ is executed each time i call my instance.
# To understand why ncalls increase :
def passer():
    pass
# %%
Profiled(passer)() # no increase because i create a new instance each time
# %%
def passer2():
    pass
passer2 = Profiled(passer2)
# %%
passer2() # increase because passer2 is now an instance of Profiled. The decorator does that
# %% [markdown]
# # Make your class decorator method compatible
#%%
class Test:
    @Profiled
    def fail(self):
        print(42)


Test().fail() # error ! why ? 
# %%
"""
If we decompose : we have fail = Profiled(fail) which means fail is now an attribute of Test. When I access Test().fail(), it calls the __get__ method of the fail attribute..
In conclusion, if you define a decorator as a class, you need to implement the __get__ method in order to use it inside other classes
"""

class Profiled2:
    def __init__(self, func): # same
        wraps(func)(self)
        self.ncalls = 0

    def __call__(self, *args, **kwargs): #same
        self.ncalls += 1
        print("CALL", self.ncalls)
        return self.__wrapped__(*args, **kwargs)

    def __get__(self, instance, cls):
        print("self", self)
        print("instance", instance)
        print("cls", cls)
        if instance is None:
            return self
        else:
            return types.MethodType(self, instance)
            # creates a bound method object to supply the self argument to the method


# %%
class Foo:
    @Profiled2
    def foo(self):
        print("foo")


# %%
f = Foo()
# %%
f.foo()
# %%
Foo.foo(f)
# %%
class Bar:
    @classmethod
    @Profiled2
    def bar(cls):
        print("bar")
# %%
Bar.bar()
# %%
Bar().bar()

# %%

class Baz:
    @staticmethod
    @Profiled2
    def baz():
        print("baz")

# %%
Baz.baz()
# %%
Baz().baz()
# %% # sttic method dont call the get
"""
Further investigation needed on the __get__ and types.MethodType
"""
# %%
"""
Exercise : rewrite the Profiled2 decorator as a function decorator
"""
# %%




























# %%
def profiled2(func):
    ncalls = 0
    @wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal ncalls
        ncalls +=1
        print("CALL", ncalls)
        return func(*args, **kwargs)

    return wrapper

@profiled2
def passtime():
    pass

# %%
passtime()
# %%
