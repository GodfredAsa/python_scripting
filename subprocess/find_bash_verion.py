import subprocess
import re
import os


def find_bash_version_linux():
    cmd = "bash --version".split()
    sp = subprocess.Popen(cmd, shell = False, stdout = subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    rc =  sp.wait()

    out, err = sp.communicate()
    if rc==0:
        for each_line in out.splitlines():
            if 'version' in each_line and 'release' in each_line:
                value = each_line.split(" ")[3].split('(')[0]
                print(f'Bash Version: {value}')
    else:
        print(f'Error: {err}\n Error occurred')
        
        
 


def find_java_version():
    cmd = "java -version".split()
    sp = subprocess.Popen(cmd, shell = False, stdout = subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    rc =  sp.wait()
    err, output = sp.communicate()
    if rc ==0:
       print(output)
    else:
        print(f'Output: {err}')
    

find_bash_version_linux()
print("<==----------------------------------------------------------------------------------==>")
find_java_version()
print("<==----------------------------------------------------------------------------------==>")
