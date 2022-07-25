from os import listdir
from os.path import isfile, join

# NOTE: When using, change strings
initial_string = 'Replace\nmultiple\nlines'
final_string = ('Another\nset\nof\nlines')

file_path = "/home/robby/Documents/code_testing/test_replace_example.py"

fin = open(file_path, "rt")

data = fin.read()
data = data.replace(initial_string, final_string)
fin.close()

fin = open(file_path, "wt")

fin.write(data)
fin.close()

print("Update Complete")


def function_1():
    pass
