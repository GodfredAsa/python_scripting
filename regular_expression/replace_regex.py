import re
from pprint import pprint

print('================= SUB SYNTAX =====================')
# sub(pattern, replacement_word, text or statement)
# to read more help(re.sub)
# NB: subn() returns a tuple on the result 
# where it tells you the number of replacement done

text = "This is for python2 and there are two major versions of python and python3 and in the future python4"

pattern = r'\bpython[23]?\b'
match_ob = re.sub(pattern,"jython", text, re.I)

pprint(match_ob)

match_ob = re.subn(pattern,"jython", text, count=3)
pprint("============= subn ==============")
pprint(match_ob)