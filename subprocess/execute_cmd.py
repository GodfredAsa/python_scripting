import subprocess
import os
os.system("cls")
#  command as a string sample below 

cmd = "ls -lrt"
sp = subprocess.Popen(cmd, shell= True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
rc = sp.wait()
out, err = sp.communicate()

# splitlines help return output as list 
print(f'Return Code: {rc}')
print(f'Output Code: {out}')
print(f'Error Code: {err}')







# TAKING COMMAND AS A LIST, APPLY SPLIT ON THE STRING AS A COMMAND
'''cmd = "echo $HOME".split()
sp = subprocess.Popen(cmd, shell= False, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
rc = sp.wait()
out, err = sp.communicate()

# splitlines help return output as list  
print(f'Return Code: {rc}')
print(f'Output Code: \n{out.splitlines()}')
print(f'Error Code: \n{err.splitlines()}')

'''
