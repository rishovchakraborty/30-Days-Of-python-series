# Regular Expressions
#
# A regular expression or RegEx is a special text string that helps to find
# patterns in data. To use RegEx in Python we import the built‑in `re` module.
#
# Common functions:
# - re.match()   → match only at the START of a string
# - re.search()  → find the FIRST match anywhere in the string
# - re.findall() → return a LIST of all matches
# - re.split()   → split a string using a pattern
# - re.sub()     → replace all matches with another string

import re

text = "I love python and it's so easy. python is an interpreted lang."
pattern = r"python"

# -----------------------------
# re.match
# -----------------------------
match = re.match(pattern, text)
print(match)  # "python" is not at index 0, so this prints None.

pattern2 = r"I lov"
match = re.match(pattern2, text)
print(match)  # <re.Match object; span=(0, 5), match='I lov'>

# -----------------------------
# re.search
# -----------------------------
match = re.search(pattern, text)
print(match)         # <re.Match object; span=(7, 13), match='python'>
print(match.span())  # (7, 13)
print(match.span()[0])

# -----------------------------
# re.findall
# -----------------------------
all_pythons = re.findall(pattern, text)
print(all_pythons)  # ['python', 'python']

email_text = "Contact us at support@example.com or sales@example.org"
emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", email_text)
print(emails)  # ['support@example.com', 'sales@example.org']

# -----------------------------
# re.split
# -----------------------------
csv_line = "apple,banana ,  mango,orange"
parts = re.split(r"\s*,\s*", csv_line)
print(parts)  # ['apple', 'banana', 'mango', 'orange']

# -----------------------------
# re.sub
# -----------------------------
ugly = "Python   is\tawesome\n!"
clean = re.sub(r"\s+", " ", ugly)  # collapse all whitespace into single spaces
print(clean)  # 'Python is awesome !'

# Regular Expressions

# A regular expression or RegEx is a special text string that helps to find patterns in data. A RegEx can be used to check if some pattern exists in a different data type. To use RegEx in python first we should import the RegEx module which is called re.


# re.match(): searches only in the beginning of the first line  of the string and returns matched objects if found, else returns None.
# re.search: Returns a match object if there is one anywhere in the string, including multiline strings.
# re.findall: Returns a list containing all matches
# re.split: Takes a string, splits it at the match points, returns a list
# re.sub: Replaces one or many matches within a string

# syntax
# re.match(substring, string, re.I)
# substring is a string or a pattern, string is the text we look for a pattern , re.I is case ignore


import re
text='I love python and It\'s so easy. python is an interpreted lang.'
pattern='python'

match = re.match(pattern,text)
print(match) # "python" is not at index 0, so re.match() fails.

pattern2 = 'I lov'
match = re.match(pattern2,text)
print(match) # <re.Match object; span=(0, 5), match='I lov'>

match=re.search(pattern,text)
print(match) # <re.Match object; span=(7, 13), match='python'>
print(match.span()) # (7, 13)
print(match.span()[0])

