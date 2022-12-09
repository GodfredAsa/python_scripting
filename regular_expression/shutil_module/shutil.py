# import shutil

src = "/c/Users/User/Desktop/current studies/python_scripting/python_scripting/regular_expression/shutil/file.py"
destination = "/c/Users/User/Desktop/current studies/python_scripting/python_scripting/regular_expression/shutil/file.py"

#  OPERATIONS WITH SHUTIL
# 'copy', 'copy2', 'copyfile', 'copyfileobj', 'copymode', 'copystat', 'copytree',

# 1. copyfile

# shutil.copyfile(src, destination)




# Python program to explain shutil.copyfile() method
 
# importing shutil module
import shutil
 
# Source path
# source = "/home/User/Documents/file.txt"
 
# # Destination path
# destination = "/home/User/Documents/file.txt"
 
# Copy the content of
# source to destination
shutil.copyfile(src, destination)