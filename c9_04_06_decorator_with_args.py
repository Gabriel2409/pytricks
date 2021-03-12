# %%
"""
Decorator with args
Modify a decorator at run time with nonlocal
Manually set decorator vars
Optional args
"""
#%%
from functools import partial, wraps
def print1(func):
	@wraps(func)
	def wrapper(*args, **kwargs):
		print(1)
		result = func(*args, **kwargs)
		return result
	return wrapper

@print1
def passer():
	pass

passer()
# %%
from functools import wraps
def print2(func):
	@wraps(func)
	def wrapper(*args, **kwargs):
		print(2)
		result = func(*args, **kwargs)
		return result
	return wrapper

@print2
def passer():
	pass

passer()
# %% Do we have to create a decorator for each value ?
# No, you can pass args to a decorator ! Did you notice @wraps(func) ?

def printn(n):
	def decorate(func):
		@wraps(func)
		def wrapper(*args, **kwargs):
			print(n)
			result = func(*args, **kwargs)
			return result
		return wrapper
	return decorate

@printn(8)
def passer():
	pass

passer()
# %% Lets decompose
def passer2():
	pass

printn(8) # returns a function (decorate)
printn(8)(passer2) # is the decorated function
printn(8)(passer2)()

# %% Now lets create a decorator which counts the number of times a function is called

def countcall(n):
	def decorate(func):
		@wraps(func)
		def wrapper(*args, **kwargs):
			nonlocal n
			n = n+1
			print(n)
			result = func(*args, **kwargs)
			return result
		return wrapper
	return decorate

@countcall(0)
def passer():
	pass

# %%
passer()
# %%
# Lets look at this func

def logged(logmsg="info"):
	def decorate(func):
		@wraps(func)
		def wrapper(*args, **kwargs):
			print(logmsg)
			return func(*args, **kwargs)

		def get_msg():
			return logmsg
		wrapper.get_msg_attr = get_msg

		def set_msg(newmsg):
			nonlocal logmsg
			logmsg = newmsg

		wrapper.set_msg_attr = set_msg


		return wrapper
	return decorate

@logged("warning")
def passer():
	pass

passer()
# %%
passer.get_msg_attr() # it works because we attached the get_msg_attr to the wrapper
# %%
passer.set_msg_attr("error")
passer()
# %% Note that set and get still work even if you stack decorators : remember we updated the __dict__ with @wraps(func)
@printn(5)
@logged("warning")
def passer():
	pass

passer()
# %%
passer.get_msg_attr()
# %%
passer.set_msg_attr("info")
passer.get_msg_attr()

# %% So what we saw is that you can create decorators with specific args and modify them at run time when needed. Below is the same idea but with a general pattern you can reuse
from functools import partial
def attach_wrapper(obj, f=None):
	if f is None:
		return partial(attach_wrapper,obj)
	setattr(obj, f.__name__, f)
	return f


def logged(logmsg="info"):
	def decorate(func):
		@wraps(func)
		def wrapper(*args, **kwargs):
			print(logmsg)
			return func(*args, **kwargs)

		@attach_wrapper(wrapper)
		def get_msg():
			return logmsg

		@attach_wrapper(wrapper)
		def set_msg(newmsg):
			nonlocal logmsg
			logmsg = newmsg


		return wrapper
	return decorate

@logged("warning")
def passer():
	pass
passer.set_msg("startup")
passer()
# %% the idea is similar to @wraps(func)
# first attach_wrapper(wrapper) returns partial(attach_wrapper,wrapper)
# then set_msg is decorated, which means it is the same as writing 

set_msg = partial(attach_wrapper,wrapper)(set_msg)
# which is equivalent to 
set_msg = attach_wrapper(wrapper, set_msg)
# wich is the same as writing
set_msg = set_msg
wrapper.set_msg = set_msg

# %% Why is it so complicated ?
# Why not do that for basic access ?

def logged(logmsg="info"):
	def decorate(func):

		@wraps(func)
		def wrapper(*args, **kwargs):
			print(wrapper.logmsg)
			return func(*args, **kwargs)

		wrapper.logmsg = logmsg

		return wrapper
	return decorate


@logged("warning")
def passer():
	pass


passer()
passer.logmsg # it seems to work !
# %%
passer.logmsg = "info"
passer()
passer.logmsg
# huh, so it works ?
# %%
@print2
@logged("error")
def passer():
	pass
# %%
passer()
passer.logmsg
# %%
passer.logmsg = "debug"
passer() # because we were fored to use wrapper.logmsg, it is shadowed if we stack decorator. Therefore, if you modify the attribute, it is not propagated to the code. You are better of using the accessor and setter methods shown above
# %% 
# * Optional args
# Problem : you want to create a decorator with only optional args. When no args is passed, you want the decorator to work even with no parenthesis

@logged() # this works
def passer():
	pass
passer()
# %%
@logged # this does not work
def passer():
	pass
passer()
# %%
# solution : you dont need the decorate(func) anymore because func in passed as an arg
def logged(func=None, logmsg="info"):
	if func is None:
		return partial(logged, logmsg=logmsg)
	@wraps(func)
	def wrapper(*args, **kwargs):
		print(logmsg)
		return func(*args, **kwargs)

	return wrapper


@logged(logmsg="warning") # this works
def spam():
	print('spam')
spam()
# %%
@logged() # this also works
def spam():
	print('spam')
spam()
# %%
@logged # this works too
def spam():
	print('spam')
spam()
# %%
