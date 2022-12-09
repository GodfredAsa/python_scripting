import re

text = "this 12-05-1987 is python and it is easy to learn 12-05-1986 fred@epals.com 168.100."
text2= """
this 12-05-1987 is python and it is easy 168.100.230.023 168.10.23.023 168.100.2.23
168.100.2.2399
"""
my_pattern="is"

print(re.findall(my_pattern, text))

# finding is and it in a text 
print(re.findall('i[st]', text))
# search dates 
print(re.findall('[0-9]{2}\\-[0-9]{2}\\-[0-9]{4}', text))

# search emails
print(re.findall('[a-z]{2,30}\\@epals.com', text))

print(re.findall('\d+\.\d+\.\d+\.\d+', text2))


# CASE INSENSITIVE REGEX, re.I or re.IGNORECASE
text = "this is a string, This is a new string THIS"
pattern = r'this'
print(re.findall(pattern, text, re.IGNORECASE))
# ['this', 'This', 'THIS']

# MULTILINE TEXT REGEX 
# re.M useful when reading from files or file operation
print("=================  MULTI LINE, START WORD: THIS  ==================")
multi_line_text = """this is a string
this is the second line 
This is the third line 
asfasd this"""
pattern = r'^this'
print(re.findall(pattern, multi_line_text, re.M|re.I))

# ['this', 'this', 'This']
# this at the end of a sentence in a multi line 
print(re.findall('this$', multi_line_text, re.M|re.I))







