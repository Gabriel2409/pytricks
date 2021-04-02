#%%
"""
feed a text or binary string to code that was written to handle file objects
"""
#%%
import io
s = io.StringIO()
s.write("Hello world")
print("myjam", file=s)
# %%
s.getvalue()
# %%
t = io.StringIO("Second test")
# %%
t.read(3)
# %%
t.read()
# %%
b = io.BytesIO()
b.write(b"Binary data")
b.getvalue()
# %%
