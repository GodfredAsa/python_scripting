import re
from pprint import pprint
# THE MAJOR DIFFERENCE BTN FINDALL AND FINDITER IS:
"""
FIND ALL: returns a list of the items found without any further information
about the position or lenght of each item

FINDITER - WILL ALWAYS RETURN AN OBJECT WITH MATCH OR NOT
"""

print('================= FINDITER SYNTAX =====================')
text = "This is for python2 and there are two major versions python and python3 and in the future python4"

pattern = r'\bpython[23]?\b'
match_ob = re.finditer(pattern, text)
python = [{'name': p.group(), 'start_index': p.start(), "end_index": p.end()} for p in re.finditer(pattern, text)]

pprint(python)

