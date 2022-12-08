# SEARCH LOOKS THROUGH THE ENTIRE STRING AND RETURNS THE FIRST MATCH

import re 

text = "This is for python2 and there are two major versions python and python3 and in the future python4"

pattern = r'\bpython[23]?\b'
match_ob = re.search(pattern, text)
if match_ob:
    print(f'match from pattern: {match_ob.group()}')
    print(f'starting index of match: {match_ob.start()}')
    print(f'ending index of match: {match_ob.end()}')
    print(f'length of match: {match_ob.end() - match_ob.start()}')
else:
    print(f'No match found for the pattern')
    
#  THE MATCH ONLY LOOKS AT THE FIRST WORD IN A SINGLE LINE.
# BY DEFAULT MATCH ONLY LOOKS AT THE FIRST LINE AND FOLLOWS THE SAME SYNTAX AS THE SEARCH 

print('================= MATCH SYNTAX =====================')
text = "python2 This is for python2 and there are two major versions python and python3 and in the future python4"

pattern = r'\bpython[23]?\b'
match_ob = re.match(pattern, text)
if match_ob:
    print(f'match from pattern: {match_ob.group()}')
    print(f'starting index of match: {match_ob.start()}')
    print(f'ending index of match: {match_ob.end()}')
    print(f'length of match: {match_ob.end() - match_ob.start()}')
else:
    print(f'No match found for the pattern')