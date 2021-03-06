#%%
import sys
import time
import traceback
# * Supporting with with our own object : https://docs.python.org/3/reference/datamodel.html#context-managers

class myOwnClassToOpenFiles:

    def __init__(self,name):
        """We need the name argument so that we can instantiate it with the name of the file we want to open"""
        self.name = name

    def __enter__(self):
        """ Here we return the file we just opened"""
        self.file = open(self.name, 'w')
        print(f"OPENING FILE {self.name:s}")
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Things to execute on exit. The three parameters describe the exception that caused the context to be exited. 
        If the context is executed normally, they will be none

        Args:
            exc_type : for ex TypeError
            exc_val : for ex Invalid Format
            exc_tb : the full traceback 
        """		
        if self.file:
            self.file.close()
            print (f"CLOSING FILE {self.name:s}")
        if exc_type:
            print("Exception Type", exc_type)
            print("Exception Value", exc_val)
            print("Exception Traceback", traceback.print_tb(exc_tb))
# Note that the traceback module is made to pprint exceptions
#%%
with myOwnClassToOpenFiles("jambon.txt") as f:
    f.write("test")

#%%
# same as 
opener = myOwnClassToOpenFiles("chorizo.txt")

try:
    opener.__enter__()
    opener.file.write("rr")
finally:
    opener.__exit__(None, None, None)
#%%

with myOwnClassToOpenFiles("jambon.txt") as f:
    print(undefined)

#%%
opener2 = myOwnClassToOpenFiles("chorizo.txt")
try:
    opener2.__enter__()
    print(undefined)
finally:
    print(sys.exc_info())
    opener2.__exit__(*sys.exc_info())
#%%
# * Exercise 1 : Indenter
# What if i want to implement a context manager that support indenting

class Indenter:
    def __init__(self):
        self.level = 0

    def print(self, text):
        text = '\t' * self.level + text
        print(text)

    def __enter__(self):
        self.level +=1
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.level -=1


with Indenter() as i:
    i.print("Indent")
    with i:
        i.print("Indent2")
    i.print("Indent")


#%%
# * Exercise 2 : Timer

class myTimer:
    def __init__(self):
        pass

    def __enter__(self):
        self.entertime = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        finaltime = time.time()
        print(f"Execution time: {finaltime - self.entertime}s")


with myTimer():
    for i in range(10000000):
        pass
#%%
# * WIth contextlib : context manager implements 

from contextlib import contextmanager

@contextmanager
def open_file(name):
    try:
        f = open(name, "w")
        yield f
    finally:
        f.close()

with open_file("boo.txt") as f:
    f.write("aaaa")



#%%
@contextmanager
def timer():
    try:
        entertime = time.time()
        yield
    finally:
        finaltime = time.time()
        print(f"Execution time: {finaltime - entertime}s")

with timer():
    for i in range(10000000):
        pass

#%%
# does not work well :  cant reuse already instanciated 
@contextmanager
def indent():
    level = 0
    try:
        level +=1
        print(level)
        yield
    finally:
        level -=1

# For indentation it is not possible. The contextmanager dont allow access to inner funcs and you cant to sometihing like
with indent() as i:
    with i:
        pass

# %%
import traceback
def err_func_2():
    print(undefined)

def err_func():
    err_func_2()

def encapsulate():
    err_func()

# %%
encapsulate()
# %% try except works if the error is from a child function
try:
    encapsulate()
except:
    print("except")
    traceback.print_exception(*sys.exc_info())
    # raise

# %%
