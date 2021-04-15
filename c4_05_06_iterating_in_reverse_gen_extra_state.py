#%%
"""
no need to define next if you use yield in __iter__
__reversed__ keyword
extra state
"""

for el in reversed([1,2,3]):
    print(el)
# %%
class CountDown:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        n = self.start
        while n >=0:
            yield n
            n -=1

    def __reversed__(self):
        n = 1
        while n <= self.start:
            yield n
            n +=1

for el in CountDown(5):
    print(el)
# %%
for el in reversed(CountDown(5)):
    print(el)
# %%
# * define a generator with extra state. 
# * Instead of doing everything with a function, remember that you can write your generator code inside the __iter__ of a class (instead of using nonlocal for ex...)

class GenExtra:
	def __init__(self):
		self.value = 8

	def __iter__(self):
		for i in range(0,6,2):
			yield i

aa = GenExtra()
for el in aa:
	print(el)

# %%
aa.value
# %%
# %%
