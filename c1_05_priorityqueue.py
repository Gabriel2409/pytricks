#%% [markdown]
# # Priority queue
# %%
import heapq
class MyPriorityQueue:
	def __init__(self):
		self._queue = []
		self._index = 0

	def push(self, item, priority):
		heapq.heappush(self._queue, (-priority, self._index, item))
		self._index += 1
	
	def pop(self):
		return heapq.heappop(self._queue)

class Item:
	def __init__(self, name):
		self.name = name
	def __repr__(self):
		return f"Item({self.name!r})"

# %%
q = MyPriorityQueue()
q.push(Item("P1"),1)
q.push(Item("P1"),1)
q.push(Item("P6"),5)
q.push(Item("P7"),5)
q.push(Item("P8"),1)
# %%
q.pop()
# %%
q.pop()
# %%
q.pop()
# pop returns items with highest priority by order of insertion
#%%
from queue import PriorityQueue
q2 = PriorityQueue()
dir(q2)
# %%
q2.put((2, "zzz"))
q2.put((2, "aaa"))
q2.put((1, "bbb"))
q2.put((1, "yyyy"))
q2.put((4, "ccc"))
q2.put((3, "ddd"))

while not q2.empty():
	next_item = q2.get()
	print(next_item)

# %%
