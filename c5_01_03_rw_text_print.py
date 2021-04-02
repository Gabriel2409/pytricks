#%%
"""
read file
write to file
redirect print
encoding
change print separator
"""
#%%[markdown] 
# # Read an write text data
# %% 
# * Read the entire file as a single string
with open("lorem.txt", "rt") as f:
	data = f.read()
# %%
data
# %%
# * Iterate over the lines of a file
with open("lorem.txt","rt") as f:
	for line in f:
		print(line)

# %%
# * write chunks of text data
with open("ipsum.txt", "wt") as f:
	f.write("Donec placerat sit amet arcu nec consectetur.\n")
	f.write("Mauris quis nisi vel ipsum mattis lacinia ac ut leo.\n")
	f.write("Maecenas volutpat fringilla sapien in euismod.\n")
# %%
# * or redirect a print statement
with open("ipsum.txt", "wt") as f:
	print("Etiam eget posuere lacus, sit amet imperdiet odio.", file=f)
# %%
# fails if file is opened in byte mode
with open("ipsum.txt", "wb") as f:
	print("Etiam eget posuere lacus, sit amet imperdiet odio.", file=f)
# %%
# * append at the end of file
with open("ipsum.txt", "at") as f:
	print("append1", file=f)
	f.write("append2")
# %%
#* encoding
# %%
import sys
sys.getdefaultencoding()
# %%
"""Python understands hundreds of text encodings : most common are ascii, latin-1, utf-8 and utf-16. 
utf 8 is usually a safe bet if working with web app
ascii : 7 bit characters in the range U+0000 to U+007F
latin-1 : direct mapping of bytes 0-255 to unicode character U+0000 to U+00FF
latin-1 encoding will never produce a decoding error when reading text of a possibly unknown encoding. Reading a file as latin-1 might not product a completely correct text decoding though but if you later write the data back out, the original input data will be preserved"""
# %%

with open("lorem.txt", "rt", encoding="latin-1") as f:
	print(f.read())

# %%
# * newline
"""
recognition on newline on Unix : \n
on windows : \r\n
By default python operates on a "universal newline" mode : all common newlines conventions are recognized and transformed into a single newline character (by default \n on unix and \r\n on windows)
If you dont want this translation supply newline='' to open
"""

# %%
with open("ascii_error.txt", "rt", encoding="ascii") as f:
	data = f.read()
# %%
with open("ascii_error.txt", "rt", encoding="ascii", errors="replace") as f:
	data = f.read()
data
# %%
# %%
print('first', 'second', 'third', sep="<(-_-)>")
# %%
