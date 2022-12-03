"""
FINDS FILES WHOSE CREATED DATE IS MORE THAN 3 DAYS OLD
1 ask the user to enter a file path
2. if the path entered is error exits the program 
3. if the path is a file exits the program
4. if path is correct returns the lists of files with 
older than 3 days from the time of creattion 

"""
import os 
import sys
from datetime import datetime


os.system("cls")
print(os.getcwd())

current_date = datetime.now()

req_path = input("Enter a path: ")

if not os.path.exists(req_path):
    print("Enter a valid path")
    sys.exit(1)
if os.path.isfile(req_path):
    print("Enter a directory")
    sys.exit(2)
    
for each_file in os.listdir(req_path):
    each_file_path = os.path.join(req_path, each_file)
    if os.path.isfile(each_file_path):
        file_creation_date = datetime.fromtimestamp(os.path.getctime(each_file_path))
        diff_days = (current_date -  file_creation_date).days
        if diff_days > 3:
            print(each_file_path, diff_days)