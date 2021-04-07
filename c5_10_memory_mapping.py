#%%
"""
memory map a binary file into a byte array : can be used to modify an existing file or access part of it
use of context manager
memory view
"""
#%%
import os
import mmap


def memory_map(filename, access=mmap.ACCESS_WRITE):
    size = os.path.getsize(filename)
    fd = os.open(filename, os.O_RDWR)
    return mmap.mmap(fd, size, access=access)

# creation of a file
size = 1000000
with open("data", "wb") as f:
    f.seek(size-1) # sets the file current position
    f.write(b"\x00")
# %%
# memory map func
m = memory_map("data")
len(m)
# %%
m[0:10]
# %%
# reassign a slice
m[0:11] = b"Hello World"
m.close()
# %%
# Verify the changes were saved
with open("data", "rb") as f:
    print(f.read(15))
# %%
with memory_map("data") as m:
    print(len(m))
    print(m[0:5])
# %%
# file is closed correctly
m.closed
# %%
"""By default, the memory_map function opens a file for both read and write : any modif made to the data is copied back to the original file. For read only access, supply mmap.ACCESS_READ as the access arg
To modify the data locally but not copy the changes back to the original file, use ACCESS_COPY
Can be used as an alternative to transfer data between two interpreters !
"""
with memory_map("data") as m:
    with memoryview(m).cast("I") as v:
        v[0] = 7
        print(v[0])
        print(m[0:2])
# %%
