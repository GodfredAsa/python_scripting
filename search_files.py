import os
import platform
import string

os.system('cls')
req_file = input("Enter file name searching for: ")

# WINDOWS: SEARCH FOR SYSTEM DRIVES 
def findValidDrive()-> list:
    valid_drive_paths = []
    possible_drives = string.ascii_uppercase
    for drive_name in possible_drives:
        if os.path.exists(drive_name + ":\\"):
            valid_drive_paths.append(drive_name + ":\\")
    return valid_drive_paths

def foundSearchFilePaths_onWindows() -> None:
    for each_drive in findValidDrive():
        for r, d, f in os.walk(each_drive):
            for each_file in f:
                if req_file == each_file:
                    print(os.path.join(r, req_file) )            

def foundFileSearchFiles_onLinux() -> None:
    for r, d, f in os.walk("/"):
        for each_file in f:
            if each_file == req_file:
                print(os.path.join(r, req_file) )          

def search_files_on_any_system( ) -> list:
   
    if platform.system()=="Windows":
         foundSearchFilePaths_onWindows()
    else:
        foundFileSearchFiles_onLinux()
    
        
search_files_on_any_system()