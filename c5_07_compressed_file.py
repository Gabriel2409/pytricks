#%%
"""
gzip and bz2 compression
change compression level
can work on top of file opened in binary mode
"""
#%%
import gzip
import bz2

with gzip.open("gzip_file.gz", "wt") as f:
	f.write("Gzip compression ftw")
# %%
with gzip.open("gzip_file.gz", "rt") as f:
	text = f.read()
	print(text)
# %%
with bz2.open("bz2_file.bz2", "wt") as f:
	f.write("bz2 compression ftw")
# %%
with bz2.open("bz2_file.bz2", "rt") as f:
	text = f.read()
	print(text)
# %%
# * default compression level is 9 (maximum)
# * lower levels provide better perf but not as much compression
with gzip.open("gzip_file.gz", "wt", compresslevel=5) as f:
	f.write("level 5 Gzip compression ftw")
# %%
f = open("somefile.gz", "rb")
with gzip.open(f, "rt") as g:
	text = g.read()