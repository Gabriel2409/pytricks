#%% filter elements based on a criteria
mylist = [1, 5, 9, 8, -5, -8, -5, 5, 4, -5, -2, -1, 4, 3]

#list comprehension
[n for n in mylist if n >0]
# %%
# if you don't want a large result, use a generator expression
(n for n in range(1000) if n % 2)
# %%
# what if the filtering method is too complex to be used in a comprehension ? 
values = ["1", "2", "-3.95", "-5", "NA", "4"]

def is_int(val):
	try:
		x = int(val)
		return True
	except ValueError:
		return False

for item in filter(is_int, values): # filter creates an iterator
	print(item)

# %%
