#%%
"""
How property works
The right way to use property
class and static methods
stack decorator with class and static method
lazy property
"""

#%% [markdown]
# # Classic accessor : BAD
# Note : only do this if you want to add extra funcs to get, set and delete

#%%
class Tester:
    def __init__(self, val):
        self.val = val

    def getval(self):
        print("GET")
        return self.val

    def setval(self, newval):
        print("SET")
        self.val = newval

    def delval(self):
        print("DEL")
        del self.val

t = Tester(5)
# %%
t.getval()
# %%
t.setval(8)
t.getval()
# %%
t.delval()
t.getval()
# %% [markdown]
# # Use of property (class decorator)
# Not the standard way
# %%
class Tester2:
    def __init__(self, val):
        self.val = val

    def getval(self):
        print("GET")
        return self._val

    def setval(self, newval):
        print("SET")
        self._val = newval

    def delval(self):
        print("DEL")
        del self._val

    val = property(fget=getval, fset=setval, fdel=delval, doc="val property")
# %%
tt = Tester2(45) # setter is called
# %%
tt.val
# %%
tt.val = 5
tt.val
# %%
del tt.val
tt.val
# %%
Tester2.val
# %%
Tester2.val.__doc__
# %%
# with property - alternate
class Tester3:
    def __init__(self, val):
        self.val = val

    def getval(self):
        print("GET")
        return self._val

    def setval(self, newval):
        print("SET")
        self._val = newval

    def delval(self):
        print("DEL")
        del self._val

    """val = property(fget=getval, fset=setval, fdel=delval, doc="val property")
    is the same as the 4 lines above where i instantiate property and then define the getter, setter and deleter.
    """
    val = property()
    val = val.getter(getval)
    # I can also replace the two lines above with val = property(getval)
    val = val.setter(setval)
    val = val.deleter(delval)

# %%
t3 = Tester3(45)
# %%
t3.val
# %%
t3.val = 5
t3.val
# %%
del t3.val
# %%
Tester3.val
# %%
Tester3.val.__doc__
# %%
Tester3.val.__get__(t3)
# %%
Tester3.val.__set__(t3,5)
# %%
t3.val
# %%
Tester3.val.__delete__(t3)
# %% [markdown]
# # Use of property the right way
class Tester4:
    def __init__(self, val):
        self.val = val # no _val so that init calls the setter

    @property
    def val(self):
        print("GET")
        return self._val
    # after this the method val was transformed to property(val)
    # when i try to access instance.val, it calls the __get__ of the property class. The __get__ of the property class calls the initial method which returns instance._val : so val went from method of a Tester4 instance to instance of property and returns an attribute of the Tester4 instance
    # this is why you write .val (which calls the __get__) and not .val() as val is no longer a function

    @val.setter
    def val(self, newval): #not the same val (called val' in the comments)
        print("SET")
        self._val = newval
    # after this, val is the instance of property. val has access to the setter method. A new method called val' is defined; after decoration val' = val.setter(val'). So val' is the same instance of property but now has a setter.
    # so now if i do instance.val = 5, it calls the __set__ of our property which calls val'

    # same logic applies here with __delete__
    @val.deleter
    def val(self):
        print("DEL")
        del self._val

#%%
t4 = Tester4(8)
#%%
Tester4.val.__get__(t4)
Tester4.val.__set__(t4, 9)
print(t4.val)
Tester4.val.__delete__(t4)
t4.val

"""Lots of work is needed to fully understand __get__, __set__, __delete__, __getattr__, etc. More work needed on descriptor protocol if you want something highly customizable. The difficulty lies in the fact that we will probably need to dive into the internals of python which are written in C
However, from what I understand, You should use @property if you dont want to risk breaking something
https://docs.python.org/3/howto/descriptor.html
https://realpython.com/python-descriptors/
"""
# %% [markdown] 
# # Static method and Class Method
# @staticmethod and  @classmethod are used to specify that some methods are part of the Class and not the instance. Note that they can be used by the instance as well. A classmethod is exactly the same as a staticmethod in python with the only difference that it takes the class as a first argument

class StaticMethod:
    """Emulate PyStaticMethod_Type() in Objects/funcobject.c
    and adds print of instance and owner"""
    def __init__(self, f):
        print(self)
        self.f = f

    def __get__(self, instance, owner=None):
        print("instance", instance)
        print("owner", owner)
        return self.f


class ClassMethod:
    "Emulate PyClassMethod_Type() in Objects/funcobject.c and adds print of instance and owner"""
    def __init__(self, f):
        self.f = f

    def __get__(self, instance, owner=None):
        print("instance", instance)
        print("owner", owner)
        if owner is None:
            owner = type(instance)
        def newfunc(*args):
            return self.f(owner, *args)
        return newfunc


class PDF:

    def standard(self):
        print(41)

    @StaticMethod
    def static():
        print(42)

    @ClassMethod
    def classmeth(cls):
        print(cls, 43)

# %%
PDF.standard()
# %%
PDF.static()
# %%
PDF.classmeth()
# %%
PDF().standard()
# %%
PDF().static()
# %%
PDF().classmeth()
# %%
"""
static becomes StaticMethod(static)
same as having 
class PDF:
    static = ...

So static is now an attribute of PDF. Each time it is called, it goes through the __get__

Note that, in Python, a class method is just a static method that takes the class reference as the first argument of the argument list

"""

# %%
# When a function decorator is applied to a function, it transforms it into a function. 
# When a class decorator is applied to a function, it transforms it into a callable instance.
# Which is why you can stack decorators.
# On the other hand, when you apply property, you transform your method into a class attribute which is not directly callable. classmethod and staticmethod transforms the method into a class instance where the initial method is an attribute, so not directly callable either. If you try to pass it to a decorator, it crashes

def printer(func):
    def wrapper(*args, **kwargs):
        print(42)
        return func(*args, *kwargs)

    return wrapper

class Crash:
    @printer
    @staticmethod
    def passer():
        pass

Crash.passer()
# %%
class Ok:
    @staticmethod
    @printer
    def passer():
        pass

Ok.passer()

# %%
def lazy_property(fn):
    '''Decorator that makes a property lazy-evaluated.
    '''
    attr_name = '_lazy_' + fn.__name__

    @property
    def _lazy_property(self):
        if not hasattr(self, attr_name):
            setattr(self, attr_name, fn(self))
        return getattr(self, attr_name)
    return _lazy_property

class Person:
    def __init__(self, name, occupation):
        self.name = name
        self.occupation = occupation

    @lazy_property
    def relatives(self):
        # Get all relatives
        for _ in range(100000000):
            pass

        return 5

# %%
a = Person("a","d")

# %%
a.relatives
# %%
dir(a)
# %%
class User1:
    def __init__(self, username):
        self.username = username
        self._profile_data = None
        print(f"{self.__class__.__name__} instance created")

    @property
    def profile_data(self):
        if self._profile_data is None:
            print("self._profile_data is None")
            self._profile_data = self._get_profile_data()
        else:
            print("self._profile_data is set")
        return self._profile_data

    def _get_profile_data(self):
        # get the data from the server and load it to memory
        print("Run the expensive operation")
        fetched_data = "The mock data of a large size"
        return fetched_data
# %%
u = User1(5)
# %%
u.profile_data
# %%
u.profile_data
# %%
import json
from json import JSONEncoder

class MyJSONEncoder(JSONEncoder):
    def default(self, o):
        if hasattr(o, 'toJSON'):
            return o.toJSON()
        return super().default(o)


class C:
    def __init__(self, name):
        self.name = name
    def toJSON(self):
        return {"name":self.name}

c = C("jon")
class D:
    def __init__(self, name, cc):
        self.name = name
        self.cc = cc

    def toJSON(self):
        return {"name":self.name, "cc":self.cc}


d = D("ff", c)


print(json.dumps(d, cls=MyJSONEncoder))
with open("gg.json", "w+") as fp:
        json.dump(d, fp, indent=4, cls=MyJSONEncoder)
