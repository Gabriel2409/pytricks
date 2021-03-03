#%% stacks (LIFO) : insert (push) / delete (pop )
# very similar to queue but in queues you remove the oldest item :
# a stack should be O(1) for insert and delete
# lists can be used as stack with append and pop. It is not completely O(1) because lists are dynamic arrays and the memory allocated to them can change over time
# Note that lists also provide O(1) access to random elements in them

aa = list(range(1000000))
bb = list(range(5000))
# %%
%%timeit -n 500
aa.pop() # pop a big list takes same time as short one
# %%
%%timeit -n 500
bb.pop()
# %%
%%timeit -n 500
del aa[0] # a lot slower : O(n) as the elements must be shifted to make room for other elements
#%%
%%timeit -n 500
aa.extend([0,1]) # note that extend is also very fast
# %%
%%timeit -n 500
del bb[0] 
# %%
%%timeit -n 500
bb.insert(5,"5f")
# %%
%%timeit -n 500
aa.append(1)
# %%
%%timeit -n 500
bb.append(1)
# %%
%%timeit -n 500
bb[100] = 8
# %%
%%timeit -n 500
aa[10000]
# %%
# In conclusion, python lists make very good stacks BUT sometimes its performance is inconsistent (amortized O(1))
a = [1]
# %%
%%timeit -n 1
a.append(1)

# %%
# deque make great stacks and queues : in fact deque means double queue
from collections import deque
v = deque([1])
# %%
%%timeit -n 1
v.append(1)
# %%
vv = deque(range(100000))
ll = list(range(100000))
# %%
%%timeit -n 500
vv.append(5)
# %%
%%timeit -n 500
vv.appendleft("d5") # a lot faster than a list
# %%
%%timeit -n 500
vv.popleft()
# %%
%%timeit -n 500
vv.insert(5000,"ff")
# %%
%%timeit -n 500
vv.insert(0,"ff") # better than a list
# %%
%%timeit -n 500
vv[5000] # deque has slower read access
# %%
%%timeit -n 500
ll[5000]
# %%
# ** conclusion : if you are looking for a stack or queue datastructure, deque are for you !
