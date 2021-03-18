# %% [markdown] try catch
"""
Finally execution
catching exceptions
with statement intro
"""
# %%
def example1():
    try:
        print(undefined_var)
    finally:
        print("Executed in the finally block")
example1()
# %%
def example2():
    try:
        print("defined")
    finally:
        print("Executed in the finally block")

example2()
# %%
def example3():
    try:
        print(undefined_var)
    except:
        print("The error was caught")
    finally:
        print("Executed in the finally block")

example3()
# %%
def example4():
    try:
        print("defined")
    except:
        print("The error was caught")
    finally:
        print("Executed in the finally block")

example4()
# * finally is executed after the try except statement. If there is an error, it first goes through the except statement and then in the finally block. If there is no except statement or if the error is raised again in the except, the code in finally is executed BEFORE the error is raised
# %%
# Bonus catch the right error

def example5():
    try:
        print(undefined_var)
    except NameError:
        print("The error was caught")
example5()
# %%
def example6():
    try:
        print(undefined_var)
    except ValueError:
        print("The error was caught")

# Bonus raise after catch : execute code only if there is an error (not the same as finally : why ? Because finally executes whether or not the try statement is successful or not
example6()


# %%
def example7():
    try:
        print(undefined_var)
    except:
        print("The error was caught and we will raise it again")
        raise

example7()
# %% [markdown]
# # :Bonus the with statement
# %%
def example8():
    with open("jambon.txt", "w") as f:
        f.write("beurre")

def example8bis():
    f = open("jambon.txt", "w")
    f.write("beurre")
    f.close()

# ? example8 and example8bis : do they really do the same thing ? 
# ? What if we change w with r

def example9():
    with open("jambon.txt", "r") as f:
        f.write("beurre")

def example9bis():
    f = open("jambon.txt", "r")
    f.write("beurre")
    f.close()


# %%
example8()
# %%
example8bis()
# %%
example9()
# %%
example9bis()
# %%


# * You guessed it the f.close is not executed in example9bis. In fact if i want to achieve the same result as example8, i should write:
# * This guarantees the file is closed even if an error occurs.
def example8ter():
    f = open("jambon.txt", "w")
    try:
        f.write("beurre")
    finally:
        f.close()




# example1()
# There was an error but the code in the finally block was executed nonetheless. The error was then propagated

# example2()
# No error : code in the finally block was executed

# example3()
# Error caught : the programm does not crash. Finally block is executed

# example4()
# No error, so it is the same as example2

# example5()
# Error was caught

# example6()
# Error was not caught

# example7()
# Error was caught and raised again

# example8()

# %%
