#%%
with open("exists.txt", "wt") as f:
	f.write("BANZAI")
# %%
# * Instead of 
import os
if not os.path.exists("exists.txt"):
	with open("exists.txt", "wt") as f:
		f.write("Hello")
else:
	print("Already exists")
# %%
# * Use :
with open("exists.txt", "xt") as f:
	f.write("Hello")
# %%
try:
	with open("exists.txt", "xt") as f:
		f.write("Hello")
except FileExistsError:
	print("Already exists")
# %%
