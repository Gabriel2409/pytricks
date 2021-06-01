#%%
"""
Intro
Basics
Accepting strings and path objects alike
Absolute vs relative paths
Accessing file path components
Check existence of file /dir
Create dir / file
Iterating over directory contents
Moving and deleting folders
"""
#%%
"""
Anatomy of the file : a file is composed of a sequence of bytes, called the file
contents.
A byte is an integer between 0 and 255. Bytes are stored on the physical storage
device. When accessing a file, these bytes are read in sequence from the disk.
When opening the file, the programmer must first convert the bytes to the appropriate
format. Fortunatly, Python does most of the work for us.

File system: A computer file system provides an abstract representation of the files stored
on the computer and interfaces with devices to control the storage and retrieval
of file data. Python interacts with the file system and is therefore limited to
what the file system can do.

File path : a file in the file system can be located with its file path, for ex
C:\Users\myfile.txt on windows or /home/mydir/myfile.txt on unix. As you can see
the separator is different on windows and unix. Fortunately, python has a library
that can handle it for us: pathlib.
Note : All of the operations shown below can also be done with the os library but
pathlib is the preferred way: it is more recent and more readable
"""
#%%
"""Basics"""
#%%

import myfakemodule
import pathlib
# * pathlib allows us to create path objects : notice the / instead of \
pathlib.Path.home()
# %%
# * If I was on linux, for exemple on WSL
# %%
# * cwd gets us the current directory
pathlib.Path.cwd()
# %%
# * I can use the / separator even on windows
pathlib.Path("C:\\Users\\Gabriel") == pathlib.Path("C:/Users/Gabriel")
# %%
# * the preferred way is to put the / outside
pathlib.Path.home() / "mydirectory" / "myfile.txt"
# %%
# ! a path is not a string !
pathlib.Path.home() == 'C:\\Users\\Gabriel'



#%%
"""Accepting strings and path objects alike"""
#%%
# %%
# * before going forward, sometimes, you need to pass the path as a string
str(pathlib.Path.home())

# %%
# * sometimes you want to accept both str and pathlib Path in your functions
pathlib.Path(pathlib.Path.cwd())

# %%
from typing import Union
def accept_str_and_path(mypath: Union[str, pathlib.Path] ):
	"""Returns the parent directory as a pathlib Path"""
	return pathlib.Path(mypath).parent
#%%
accept_str_and_path("C:\\Users\\Gabriel")
# %%
accept_str_and_path(pathlib.Path.cwd())
# %%
# ! WINDOWS PATH ARE CASE INSENSITIVE, AND PATHLIB chooses sometimes to display c or C so be careful when comparing to a string
print(pathlib.Path.cwd())

str(pathlib.Path.cwd()) == 'C:\\Users\\Gabriel\\Documents\\workprojects\\pythontricks'
# %%
# ! is is better to do 
pathlib.Path.cwd() == pathlib.Path('C:\\Users\\Gabriel\\Documents\\workprojects\\pythontricks')

#%%
"""Absolute vs relative paths"""
path = pathlib.Path("photos/images")
print(path.is_absolute())
# %%
path = pathlib.Path("C:/photos/images")
print(path.is_absolute())
# %%
# * resolve tries to return an absolute path
pathlib.Path("/Users/Gabriel").resolve()
# %%
# * but can fail and return a relative path on failure so dont rely on it too much
pathlib.Path("Users/Gabriel").resolve()
#%%

"""
Accessing file path components
"""
#* parents return an iterable containing the path of the parent, the grandparent, the grand grand parent, etc..
path = pathlib.Path.cwd()
list(path.parents)
# %%
# which means
path.parents[0] # equivalent to cd ..
# %%
path.parents[1] # equivalent to cd ../..
# %%
path.parents[2] # equivalent to cd ../../..
# %%
path.parents[8] # ? what will I get ?
#%%
path.parent # equivalent to parents[0]
#%%
#* anchor
path.anchor # returns root folder as a string, not a path object

#%%
# * stem, name and extension. 
# ? Remember using os with splittext to get the extension ? 
current_file_path = pathlib.Path(__file__)
current_file_path
#%%
current_file_path.name # * gets the name of the file
#%%
current_file_path.stem # * gets the name of the file without extension
#%%
current_file_path.suffix # * gets the extension of the file with the .
#%%
# !  be careful though, maybe it is not exactly what you want
angular_path = pathlib.Path("mydir/app.module.ts")
angular_path.name, angular_path.stem, angular_path.suffix


#%%
import myfakemodule
# * a concrete example
path = pathlib.Path(myfakemodule.__file__) # locates the __init__ of your module
path
# %%
# ? How would I access the file 01_sorting.py in my file in myfakedestination ? 


final_path = path.parents[1] / "myfakedestination" / "mysubfolder" / "myfile.txt"
# %%
final_path.exists()

# %%
"""
Check existence of file /dir
"""
final_path.exists()
# %%
final_path.is_file()
# %%
final_path.parent.is_dir()
# %%

(final_path.parent /"zgsgsgfsg").is_dir() # is_file, exists

# %%
"""
Create directory
"""
(pathlib.Path("mydir")).mkdir()
# %%
pathlib.Path("mydir2/mysub").mkdir() # cant create if parent does not exist
# %%
pathlib.Path("mydir2/mysub").mkdir(parents=True) # cant create if parent does not exist
# %%
pathlib.Path("mydir").mkdir() # cant create if dir already exists
# %%
if not pathlib.Path("mydir").exists():
	pathlib.Path("mydir").mkdir()
# %%
# same as
pathlib.Path("mydir").mkdir(exist_ok=True)
# * you can combine parents and exist_ok to make directory creation easier
# %%
"""
Create file
"""
# use the touch method
filepath = pathlib.Path("mydir")/ "myfile.txt"
# %%
filepath.touch() # no error even if file exists
# %%
# however no parents method so you have to make sure the directory exists before creating the file
(pathlib.Path("mydfgfgfgfr")/ "myfile.txt").touch()
# %%
# easy fix : 
filepath = pathlib.Path("doesnotexist")/ "nonexistant" / "myfile.txt"

# %%
filepath.parent.mkdir(parents=True, exist_ok=True)
filepath.touch()
# %%
"""Iterating over directory contents"""
for path in pathlib.Path.cwd().iterdir():
	print(path) # note that print prints the str of the path
# %%
# make it more visible
for path in pathlib.Path.cwd().iterdir():
	print(path.name)
# %%
# * filter with glob : same as iterdir but better. Filter with a pattern
for path in pathlib.Path.cwd().glob("*"): # all files / dir
	print(path.name)
# %%
for path in pathlib.Path.cwd().glob("*.txt"): # all txt files
	print(path.name)

"""
Note about patterns for glob
*  => any number of caracters, for ex *b* matches 4h5bdff but not acd
? => a single caracter, for ex ?b matches ab but not dfdfb
[abc] => matches one of the caracter, for ex a[bc] matches ac but not abc
"""
# %% 
# * recursive glob (rglob)
for path in pathlib.Path.cwd().glob("**/*.txt"): # all txt files
	print(path.name)

# %%
# same as
for path in pathlib.Path.cwd().rglob("*.txt"): # all txt files
	print(path.name)

#%%
"""Moving and deleting"""
#%%
# * replace to move / rename a file
initial_path = pathlib.Path.cwd() / "mydir" / "myfile.txt"
destination_path = pathlib.Path.cwd() / "mydir" / "changed.txt"
initial_path.parent.mkdir(parents=True, exist_ok=True)
initial_path.touch()

initial_path.replace(destination_path)
#%%
# ! be careful as this overwrites the destination path. For security, you can do
if not destination_path.exists():
	initial_path.replace(destination_path)
#%%
# * Moving / renaming a directory
mysubdir = pathlib.Path.cwd() / "mydir" / "mysubdir"
mysubdir.mkdir(exist_ok=True, parents=True)
(mysubdir / "afile").touch()
mydir2 = pathlib.Path.cwd() / "mydir2"
mysubdir.rename(mydir2)

#%%
#* copying a file : you need shutil
import shutil
myfile = pathlib.Path.cwd() / "mydir" / "file.txt"
myfile_new = pathlib.Path.cwd() / "mydir" / "file_new.txt"
myfile.parent.mkdir(exist_ok=True, parents=True)
myfile.touch()
shutil.copy(myfile, myfile_new)
#%%

# * deleting a file
myfile.unlink() # error if file does not exist : check with exists first if needed
# %%
# * deleting a directory with rmdir : only works on empty directories
myfile.parent.rmdir()
# %%
# However if you want to brute force
shutil.rmtree(myfile.parent)
# %%
