#%%
from collections import Counter


# %%
{} + {'a':5}
# %%
round(55,-2)
# %%
0.1.is_integer()
# %%
1.1.is_integer()
# %%
def manipulate_user_input():
	prompt = "Enter a number"
	inp = input(prompt)
	try:
		nb = float(inp)
		rd = round(nb,2)
		print(f"{nb} rounded to two decimal places is {rd:.2f}")
	except ValueError:
		print("A number, dumass")

# %%
manipulate_user_input()
# %%
f"{3**.125:.3f}"
# %%
f"{150000:,.2f}"

# %%
f"{2.02/10:.0%}"
# %%
(1+2j).conjugate()
# %%
f"{10:#o}"

# %%
