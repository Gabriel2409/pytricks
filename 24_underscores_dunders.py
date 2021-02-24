#%% single leading underscore _var
class Textbox:
	def __init__(self):
		self.public = "Modify me"
		self._private = "I am not really private but you may want to leave me alone"

tbox = Textbox()
print(tbox.public)
print(tbox._private)
# %%
# So i can access every var even with a leading _. It is more there to communicate the intent.
# Note that only vars and methods without _ are imported if you do a wild card import. But you should never do that.
# %%
# Trailing underscore. No real impact : useful when a keyword is already taken
def try_to_use_python_class_keyword(class):
	pass

# %%
def try_to_use_python_class_keyword(class_):
	pass
# %%
# Dunder : a dunder is a double underscore __
class WithDunder:
	def __init__(self):
		self.standard = "standard"
		self._leading = "_leading"
		self.trailing_ = "trailing_"
		self.__dunder = "__dunder"
# %%
dund = WithDunder()
print(dund.standard)
print(dund._leading)
print(dund.trailing_)
print(dund.__dunder)
# %%
# Huh, no attribute dunder ? 
dir(dund)
# %%
class Overrider(WithDunder):
	def __init__(self):
		super().__init__()
		self.standard = "overriden"
		self._leading = "overriden"
		self.trailing_ = "overriden"
		self.__dunder = "overriden"
# %%
over = Overrider()		
print(over.standard)
print(over._leading)
print(over.trailing_)
print(over.__dunder)
#%%
dir(over)
#%%
print(over._WithDunder__dunder)
print(over._Overrider__dunder)
# %%
# you can have __ with methods to
class Test():
	def __init__(self):
		pass
	def __meth(self):
		return "youpi"
print(Test()._Test__meth())

# %% Name mangling is fully transparent ! 
_GlobalAccess__dontuseme = "strange name for a var"

class GlobalAccess:
	def access(self):
		print(__dontuseme)
GlobalAccess().access()

# %%
# how to use in real life 
class Parent:
	def __init__(self):
		self.__dunder = "__dunder"
	def get_dunder(self):
		return self.__dunder # here i can access __dunder 

class Child(Parent):
	def __init__(self):
		super().__init__()
		self.__dunder = "overriden"
	def get_child_dunder(self):
		return self.__dunder # here i can access __dunder

ch = Child()
print(ch.get_dunder())
print(ch.get_child_dunder())


# %%
# __init__ is not name mangled : no name mangling for dunder before and after !
# Dont name your var with __ __ because you may conflict with future updates to python code.
# bonus : single underscore
# _ is the result of the last expression IF YOU ARE WORKING ON INTERPRETER
# Also used to say you don't care about the var
def get_vals():
	return ("important", "not_important")

(imp, _) = get_vals()
print(imp)
# %%

