#%%
"""
read and write binary data
byte integer value (indexing and iterating)
encode and decode
no conversion writing
"""
#%%
#* basic read write
with open("lorem.txt", "rb") as f:
	data = f.read()
# %%
data
# %%
with open("ipsum2.txt", "wb") as f:
	data = f.write(b"Hello world")
# %%
# * iterating 
# text
t = "Hello world"
for c in t:
	print(c)
# %%
# byte: indexing and iterating return integer byte values instead of byte strings
b = b"Hello world"
for c in b:
	print(c)
# %%
# * encode and decode
with open("ipsum2.txt", "wb") as f:
	text = "Hello world"
	f.write(text.encode("utf-8"))

# %%
with open("ipsum2.txt", "rb") as f:
	data = f.read(4)
	print(data.decode("utf-8"))
# %%
#* no conversion
import array
nums = array.array("i", [1,2,3,4])
with open("data.bin", "wb") as f:
	f.write(nums)
# %%
a = array.array('i', [0,0,0,0,0,0,0,0])
with open("data.bin", "rb") as f:
	f.readinto(a)
a
# %%
