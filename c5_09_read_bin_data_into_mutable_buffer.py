#%%
"""
read binary data into a buffer
NOTE : a bytearray is a mutable version of byte
combine it with iteration on a fixed size record
memory view
"""
#%%
import os

# * import the whole content into a mutable buffer
def read_into_buffer(filename):
	buf = bytearray(os.path.getsize(filename))
	with open(filename, 'rb') as f:
		f.readinto(buf)
	return buf

# can use pathlib: pathlib.Path("sample.bin").stat().st_sizes

with open("sample.bin", "wb") as f:
	f.write(b"Hello World")

buf = read_into_buffer("sample.bin")

# %%
# * import the whole content into an immutable byte

with open("sample.bin", 'rb') as f:
	immutable = f.read()
immutable
# %%
# unlike read, readinto fills the content of an existing buffer rather than allocating new objects and returning them. Which means we can use it to avoid  extra memory alloc
# readinto also returns the size of the returned value
record_size = 4
buf = bytearray(record_size)
with open("sample.bin", "rb") as f:
	while True:
		n = f.readinto(buf)
		if  n < record_size:
			break
		print(n, buf)
# %%
# note that we lose the final record. If I still want it, i have to do extra checks. I can for ex assign 0 on the last
record_size = 4
buf = bytearray(record_size)
with open("sample.bin", "rb") as f:
	while True:
		n = f.readinto(buf)

		if  n ==0:
			break

		if n < record_size:
			buf[n:] = b"0" * (record_size - n)
		print(n, buf)
# %%
buf = bytearray(b"What a wonderful world!")
m1 = memoryview(buf)
# %%
m2 = m1[-6:]
m2[:] = b"earth!"
# %%
buf

# Note that the size must be the same
m2[:] = b"eartddfggfgfh!"

# %%
# ! caution with readinto, always check the returned value to ensure the nb of returned bytes is the same as the record size. Otherwise, it may indicate corrupted data
# * Be on the lookout for other into functions (recv_into, pach_into): many other parts of python have support for direct I/O or data access