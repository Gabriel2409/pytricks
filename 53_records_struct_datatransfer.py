"""
namedtuples
struct
simplenamespace
"""

#%% named tuple : a good way to write more readable code by enforcing the structure of your data : you can't mispell a field
from collections import namedtuple
p1 = namedtuple("Point", "x y z")(1,2,3)
print(p1)

# %%
p1.x, p1[0]
# %%
p1.x = 5

# %%
p1.w ="r"

# %% typing NamedTuple -improved Namedtuples. Note that type is not enforced without a type checking tool like mypy
from typing import NamedTuple
class Car(NamedTuple):
	color: str
	automatic: bool
	kilometers: float

Car("red", True, 154)

# %%
Car("blue")
# %%
Car(True, "red", 1254) # not enforced ! 

# %%
Car(color="blue", kilometers=45, automatic=False)
# %% struct struct
# not intended to use only in python : more of data exchange format
from struct import Struct
MyStruct = Struct("i?f")
data = MyStruct.pack(23, False, 42.0)
print(data)
print(MyStruct.unpack(data))
# %%
# types.SimpleNamespace : SimpleNamespace instances expose all of their keys as attributes : that means we can use obj.key instead of obj["key"]. It also has a nice __repr__

from types import SimpleNamespace
sandwich = SimpleNamespace(bread="standard", sauce="mayonnaise", size=100)
print(sandwich)
# %%
print(sandwich.bread)
print(sandwich.size)
sandwich.size = 50
print(sandwich.size)

# 2-3 fields => tuple
# need for immutable fiedls => tuple, namedtuples
# need lockdown fields and avoid typos => namedtuples
# keep things simple => dict
# need full control : custom class with @property 
# need to add behavior : custom class (you can extend namedtuple or start from scratch)