
#%%
import sys
import threading
import time

def func(f,g):
    # print("hello from thread %s" % threading.current_thread().name)
    print(f,g)
    time.sleep(2)

threads = []
f = ["1","2",3]
g = ["4","5",6]
for i in range(3):
    thread = threading.Thread(target=func, args=([f[i], g[i]]))
    thread.start()
    threads.append(thread)
print(threads)
# %%

# %%
