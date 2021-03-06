#%% [markdown]
# # Priority queue
# %%
import heapq
class PriorityQueue:
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
q = PriorityQueue()
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
# %%
# pop returns items with highest priority by order of insertion