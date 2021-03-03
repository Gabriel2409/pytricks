#%%
# https://realpython.com/python-gil/
# https://realpython.com/python-memory-management/
"""The Python Global Interpreter Lock or GIL, in simple words, is a mutex (or a lock) that allows only one thread to hold the control of the Python interpreter.

This means that only one thread can be in a state of execution at any point in time. The impact of the GIL isn’t visible to developers who execute single-threaded programs, but it can be a performance bottleneck in CPU-bound and multi-threaded code.

Since the GIL allows only one thread to execute at a time even in a multi-threaded architecture with more than one CPU core, the GIL has gained a reputation as an “infamous” feature of Python."""
# %%
"""
Python uses reference counting for memory management. It means that objects created in Python have a reference count variable that keeps track of the number of references that point to the object. When this count reaches zero, the memory occupied by the object is released.
"""
# %%
import sys
a = []
b = a
sys.getrefcount(a)
# here the empty list was referenced by a, b and the argument passed to sys.getrefcount
# %%
"""Now, what if there were two different threads that decrease or increase the value of a simultaneously ? 
It can cause leaked memory that is never released or even worse, it can release the memory of an object that is still referenced. 
We could add lock to every data structure to prevent it from being modified inconsistently but if there are multiple locks, we can create a deadlock + decreased performance
"""

"""
The GIL is a single lock on the interpreter itself which adds a rule that execution of any Python bytecode requires acquiring the interpreter lock. This prevents deadlocks (as there is only one lock) and doesn’t introduce much performance overhead. But it effectively makes any CPU-bound Python program single-threaded.
"""