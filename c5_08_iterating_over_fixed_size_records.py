#%%
"""
little property of iter
alternative to line by line iteration
"""
#%%
# to use iter, you dont always need to pass an iterable
# you can also pass a callable and a sentinel value

class MyCallable:
	def __init__(self,):
		self.ncalls = 0
	
	def __call__(self):
		self.ncalls +=1
		print(self.ncalls)
		return f"I was called {self.ncalls} times"

aa = MyCallable()

for i in iter(aa, "I was called 3 times"):
	print(i)

# everything is executed in the call block but as soon as the return value becomes equal to "I was called 3 times", it raises a stop iteration

#%%
nbcalls = 0
def my_func():
	global nbcalls
	nbcalls+=1
	print("in my_func", nbcalls)
	return nbcalls

for i in iter(my_func, 5):
	print(i)
#%%
# * The idea is to use partial and f.read so that we iterate until the returned value is ""
# ! note : this is more common with binary data files. In this case, the sentinel is b""
from functools import partial
RECORD_SIZE = 32
with open("lorem.txt", "rt") as f:
	records = iter(partial(f.read, RECORD_SIZE), "")
	for r in records:
		print(r)
		print("--------")
# %%
