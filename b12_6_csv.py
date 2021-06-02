#%%
"""
Naive approach
Writing
Reading
Headers
"""
#%%
import pathlib
import csv

csv_dir = pathlib.Path.cwd() / "csv_dir"
csv_dir.mkdir(exist_ok=True)
file_path = csv_dir / "temperatures.csv"
#%%
""" Naive approach"""

temperature_readings = [-5, 12, 4, 16, -2]
temperature_readings_2 = [-8, 11, 3]

# * to write to a file, first we need to convert the list to a string with each value separated by a comma. To go to another line, we must write \n

with file_path.open(mode="w", encoding="utf-8") as file:
    # with open(filepath, mode="a", encoding="utf-8") as file:
    file.write(",".join(str(t) for t in temperature_readings))
    file.write("\n")
    file.write(",".join(str(t) for t in temperature_readings_2))

# %%
# In fact, the string that we write to the csv looks like this : "-5,12,4,16,-2\n-8,11,3". This is not very practical
with file_path.open(mode="r", encoding="utf-8") as f:
    text = f.read()
text
# %%
# Now to recover my temperatures, it is a chore
temp1_str, temp2_str = text.split("\n")

temp1 = temp1_str.split(",")
temp1  # and i get the values as strings not numbers

# %%
[int(t1) for t1 in temp1]  # finally got it

# %%
"""Writing"""
daily_temperatures = [[10, 14, 12, 13], [4, 9, -5, 5], [15, 24, 35, 45]]

# ! important to specify the newline parameter, especially on windows to avoid problems with windows incorrectly interpreting newlines
with file_path.open(mode="w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    print("csv writer object of type", type(writer))
    # * writer is our csv writer object. We will use it to write the csv to the file. Note that we will NOT use the write method from f
    for temperature_list in daily_temperatures:
        writer.writerow(temperature_list)

# * We were able to write row by row pretty easily with the writerow method. No need to convert anything.
# %%
# We can simplify even more
with file_path.open(mode="w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(daily_temperatures)

# * It also works with numpy. So next time you want to write a matrix to csv just use the writerows method : no need to use pandas
# %%
"""Reading"""

with file_path.open(mode="r", encoding="utf-8", newline="") as f:
    reader = csv.reader(f)
    print("csv  reader object of type", type(reader))
    for row in reader:
        print(row)

# * we got the rows as list of strings. It is the standard behavior, everything is by default considered a string in a csv. To get my initial matrix

#%%
with file_path.open(mode="r", encoding="utf-8", newline="") as f:
    reader = csv.reader(f)
    mat = [[int(t) for t in row] for row in reader]
mat
# %%
"""Headers"""
# * In most csvs, the first row is the header.
# first let us create a dummy csv 
employee_path = file_path.with_name("employees.csv")

employees = (
    ["name", "department", "salary"],
    ["Lee", "Operations", 25000],
    ["John", "Engineering", 50000],
    ["Maria", "CEO", 150000],
)

with employee_path.open(mode="w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(employees)

#%%
# In fact headers are so common that csv has a way to get the file contents as a dict
with employee_path.open(mode="r", encoding="utf-8", newline="") as f:
	dict_reader = csv.DictReader(f)
	print("field_names", dict_reader.fieldnames)
	print("rows:")
	for row in dict_reader:
		print(row)

# * fields names are retrieved as a list and all rows are now a dict where the key is one of the field name
# ! Note that it might be a bit tricky to skip rows
# %%
# you can specify the header : note that if your csv is a bit messy, it can cause issues
with file_path.open(mode="r", encoding="utf-8", newline="") as f:
	dict_reader = csv.DictReader(f, fieldnames= ["Day1", "Day2", "Day3", "Day4"])
	print("field_names", dict_reader.fieldnames)
	print("rows:")
	for row in dict_reader:
		print(row)
# %%
people_path = file_path.with_name("people.csv")

people = [
    {"name": "John", "age":29},
    {"name": "Maria", "age":25},
    {"name": "Diego", "age":48},
]
with people_path.open(mode="w", encoding="utf-8", newline="") as f:
	dict_writer = csv.DictWriter(f, fieldnames = people[0].keys()) # need to specify field names as a list
	dict_writer.writeheader() # return number of characters written
	dict_writer.writerows(people)
# %%
"""
Conclusion : the module is very basic. With a little bit of tweaking, you can do complicated stuff like skipping certain lines with filter, etc...
However, using pandas might be easier
The csv module is best used for simple cases
"""