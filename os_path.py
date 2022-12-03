import os
os.system('cls')
path = "C:\\Users\\User\\Desktop\\py_exercises"
# print(path)


file_path = [os.path.join(r, e) for r, d, f in os.walk(path, topdown=False) if len(f) !=0 for e in f]

print(file_path)