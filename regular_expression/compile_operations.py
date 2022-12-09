import re 
from pprint import pprint

text = "This is about python. Python is easy to learn and we have two major versions: python2 and python3"
pattern =r"\bpython[23]?\b"
pprint(re.findall(pattern, text, re.IGNORECASE))
pprint(re.split(pattern, text, re.IGNORECASE))
pprint(re.search(pattern, text, re.IGNORECASE))
       
# THE COMPILE OPERATION IS USED WHEN THE PATTERN WILL BE USED MULTIPLE TIMES IN THE CODE 
# the flags used be used in the compilation object
print("=========== Compilation approach ===========")
pattern_ob = re.compile(pattern, re.IGNORECASE)
print(pattern_ob)
print(pattern_ob.search(text))
print(pattern_ob.findall(text))
print(pattern_ob.split(text))

