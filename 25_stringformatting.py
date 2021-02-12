# %% [markdown]
# # Old style
# https://docs.python.org/3/library/stdtypes.html#old-string-formatting


# u : unicode string for backward compatibility
# r : raw string : ingnore escapte characters
import re
print("unicode\t", u"unicode\t", "unicode\t" == u"unicode\t")
print("unicode\t", r"unicode\t", "unicode\t" == r"unicode\t")
print("C\\Path", r"C\Path", "C\\Path" == r"C\Path")

# b byte
print("\xcf", b"\xcf")
print('I am a string'.encode('ASCII'))

print(b'I am a string'.decode('ASCII'))

# any combination of rf, br is allowed... f is for format, we'll see later

# so you can escape the quote but you still prints the backlash
print(r'need escape \'quote\'')

# why raw string in regex ?
# Regular expressions use the backslash character ('\') to indicate special forms or to allow special characters to be used without invoking their special meaning. This collides with Python’s usage of the same character for the same purpose in string literals..."
# %%
test_str = "I love\dpizza"

# python and regex parser both use \ to give meaning to expression
# more research is needed : does regex parser work first ?

pattern0 = r"(\dpizza)"
a0 = re.search(pattern0, test_str)
print(a0)


pattern1 = "(\\dpizza)"
a1 = re.search(pattern1, test_str)
print(a1)

pattern2 = r"(\\dpizza)"
a2 = re.search(pattern2, test_str)
print(a2)

pattern3 = "(\\\\dpizza)"
a3 = re.search(pattern3, test_str)
print(a3)


# %%
# I can use a single value or a tuple
general = "General Kenobi"
print("Hello there ! %s" % general)
tuple_vader = ("Anakin",)
"You were my brother %s !" % tuple_vader

# %%
# Multiple values : need to use tuple

verb = "underestimate"
reason = "power"
"You %s my %s !" % (verb, reason)

# %%
# or a dict (no need to put them in order)

"Let the %(verb)s flow into %(pronoun)s !" % {
    "pronoun": "you", "verb": "anger"}

# %%
# %% [markdown]

print("delimiter % / O mapping key (example) / O conversion flag / O minimum field width / O precision / O length modifier / Conversion type")

# %%
# examples
numberpos = 45.34
numberneg = -45.34
numberint = 450
print("My number is %f" % numberpos)
print("My number is %f" % numberneg)
# %%
print("My number is % f" % numberpos)
print("My number is % f" % numberneg)
# %%
print("My number is %+f" % numberpos)
print("My number is %+f" % numberneg)
# %%
print("My number is %08f" % numberpos)
print("My number is %08f" % numberneg)
print("My number is %05d" % numberint)
# %%
print("My number is %06.1f" % numberpos)
print("My number is %04.3f" % numberneg)
# %%
print("My number is %.0f" % numberint)
print("My number is %#.0f" % numberint)

# %%
# length modifier h, l, L
wide_string = "Wide String"
# From what i understand, they can be present but it is not necessary for python so they are ignored.
print("%ls" % wide_string)
print("%Ls" % wide_string)
print("%hs" % wide_string)

# %%
# small exercise
nb = 42.5789
# print this number with only two digits after . and with a + sign
print("%f" % nb)

# %%
# all the conversion flags
nbint = 42

print("%i" % nbint)
print("%d" % nbint)  # u is the same as d but is obsolete
print("%o" % nbint)  # octal value
print("%#o" % nbint)  # 42 = 8*5 +2
print("%x" % nbint)  # hexadecimal
print("%X" % nbint)  # hexadecimal upper
print("%#x" % nbint)  # hexadecimal
print("%#X" % nbint)  # hexadecimal upper

# %%
nbfloat = 420543643136456431464.335
print("%e" % nbfloat)  # hexadecimal
print("%E" % nbfloat)  # hexadecimal upper
print("%#.0e" % 0)  # alternate form : contains a . even if no digit after
print("%.0E" % 0)  # hexadecimal upper
# %%
# g is a mix of f and e (G is a mix of F and E) ! uses e if below e-4 or above e4
print("%g" % nbfloat)
print("%g" % nbint)
# %%
# c is single character : i dont really know
print("%c" % "5")


# %%

class Car():
    def __init__(self):
        pass

    def __str__(self):
        return "str car"

    def __repr__(self):
        return "repr car"


print("%r" % Car())  # uses repr
print("%s" % Car())  # uses str
print("%a" % "é")  # converts to ascii


# %% [markdown]
# # New style : https://docs.python.org/3/library/stdtypes.html#str.format
# instead of % use format
# no more tuple or dict
print("Hello {}, General {}".format("There", "Kenobi"))
# %%

print("Hello {location}, General {name}".format(
    name="Kenobi", location="There"))
# %%
# all the flags work the same way but you have to add : before
nbnew = 45.95712
print("{:f}".format(nbnew))
print("{:+.2f}".format(nbnew))
print("{nb:+.2f}".format(nb=nbnew))

# Good news : everything we did before works the same way and you won't have to try to find % on your keyboard. 

# %% [markdown]
# # Let's go further : literal string interpolation (python 3.6+)
location = "there"
print("Hello {location}")

# %%
print(f"Hello {location}")

# %%
nblit = -85.2
print(f"Number {nblit:05.0f}")
# no need to format anymore ! 
# plus you can combine f and r ! 
verb = "like"
print(fr"The linter \does not {verb:s} it though ")

# %%
# you can even do operations in f strings
a = 1
b = 2
print(f"{a}+{b}={a+b}")

# %%
# So pretty cool but can cause security issue. Never use f strings to process user inputs or even format! 
# à revoir demain

SECRET_ENV_VARIABLE = "my secret"
class ShowUserInput():

	def __init__(self):
		pass
	def show(self,inp):
		print(inp.format())

uu = ShowUserInput()
uu.show("Test")
uu.__init__.__globals__["SECRET_ENV_VARIABLE"]
# %%
uu.show({'uu.__init__.__globals__["SECRET_ENV_VARIABLE"]'})

# %%
