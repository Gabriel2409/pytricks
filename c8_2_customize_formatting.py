#%%
"""
format method
"""
class CustomDate:
	def __init__(self, year, month, day):
		self.year = year
		self.month = month
		self.day = day

	def __repr__(self):
		return f"Year:{self.year}, Month:{self.month}, Day:{self.day}"

# %%
a = CustomDate(2020,5,15)
print(a)
# %%

class CustomDatev2(CustomDate):
	def __format__(self, code):
		if code == "":
			return self.__repr__()

		if code == "ymd":
			return f"{self.year},{self.month}, {self.day}"
		elif code == "dmy":
			return f"{self.day},{self.month},{self.year}"
		elif code == "mdy":
			return  f"{self.month},{self.day},{self.year}"
# %%
b = CustomDatev2(2021,8,19)
print(b)
format(b)
# %%
print(f"{b}")
print(f"{b:mdy}")
print(f"{b:dmy}")
# %%

# %%
ff = "CustomDatev2(2021,8,19)"
eval(ff).year
# %%
