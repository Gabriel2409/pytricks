#%% [markdown]
# # keeping last N items
# %%
lines = [
    "line1",
    "line2",
    "line3 pat",
    "line4",
    "line5 pat",
    "line6 pat",
    "line7 pat",
    "line8",
    "line9 pat",
    "line10",
    "line11 pat",
    "line12 pat",
    "line13 pat",
    "line14",
    "line15 pat",
]

pattern = "pat"
# %%
# with a list it is not very easy
def listsearch(lines, pattern, history=3):
    previous_lines = []
    for line in lines:
        if pattern in line:
            print(line, previous_lines)
        previous_lines.append(line)
        if len(previous_lines) > 3:
            del previous_lines[0] # O(n) time : not good

listsearch(lines, pattern)
# %%

from collections import deque

q = deque(maxlen=5)
q.extend([1, 2, 3, 4])
print(q)
q.append(5)
print(q)
# %%
q.append(6)
print(q)
# %% Example : each time i find a match i also want to show the 3 previous lines
def search(lines, pattern, history=3):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            print(line, previous_lines)
        previous_lines.append(line) # O(1) operation
search(lines, pattern)


# %%  # ! Important note : it is common to use a generator in a search function. It allows to decouple the search from the logic applied to the found items

def gensearch(lines, pattern, history=2):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)

mygenerator = gensearch(lines, pattern)
# %%
for item in mygenerator:
    print(item)
# %% [markdown] # Finding N largest or smallest items
import heapq
import numpy as np
# heap queue or priority queue algorithm : every parent has a value less or equal to its children

a = [float(np.random.rand(1)) for _ in range(100000)]
# %%
%%timeit
a.sort()
# %%
b = [float(np.random.rand(1)) for _ in range(100000)]
# %%
%%timeit
heapq.heapify(b)
# %%
c = [float(np.random.rand(1)) for _ in range(100000)]
# %%
%%timeit
heapq.nlargest(3,c) #nsmallest
# %%
%%timeit
sorted(c)[-3:]
# %%
d = [float(np.random.rand(1)) for _ in range(100000)]
heapq.heapify(d)
heapq.heappop(d) # pops the first item and replaces it with the next smallest. O(nlogn)
# %% Note : nlargest and nsmallest are appropriate when we look for a a relatively small nb of items. If we only want 1, min and max are better. If we want to find most of the items, it is better to sort the list first. Note that nsmallest and nlargest are adaptive in the algorithm they use depending on the number
