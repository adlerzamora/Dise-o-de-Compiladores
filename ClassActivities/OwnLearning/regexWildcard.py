# In python regular expresions are supported by the re module
import re

# basic patterns: ordinary characters are the simplest regular
# expresions (they match themselves)
pattern = r"Cookie"
sequence = "Cookie"

if re.match(pattern, sequence):
    print("Match!")
else:
    print("Not a match")

# Wild Card Characters: Special Characters are characters which do not
# match themselves as seen but actually have a special meaning when used
# in a regular expression

# . - A period matches any single character except new line 
re.match(r'Co.k.e','Cookie').group()
# The group() function returns the string matches by the re.

# \w - Matches any alphanumeric character, this is equivalent to the class [a-zA-Z0-9_].
re.search(r'Co\wk\we','Cookie').group()

# \W - Matches any non-alphanumeric character, this is equivalent to the class [^a-zA-Z0-9_].
re.search(r'C\Wke', 'C@ke').group()

# \s - Matches any whitespace character, this is equivalent to the class [ \t\n\r\f\v].
re.search(r'Eat\scake','Eat cake').group()

# \S - Matches any non-whitespace character, this is equivalent to the class [^ \t\n\r\f\v].
re.search(r'Cook\Se','Cookie').group()

# \t - Lowercase t matches a tab
#re.search(r'Eat\tcake', 'Eat    cake').group()

# \n - Matches a newline
# \r - Matches return
# \d - Matches decimal digit 0-9
re.search(r'c\d\dkie','c00kie').group()

# ^ - Caret matches a pattern at the start of the string
re.search(r'^Eat','Eat cake').group()

# $ - Matches a pattern at the end of the string
re.search(r'Cake$','Eat Cake').group()

# [abc] - Matches a or b or c
#[a-zA-Z0-9] - Matches any letter from (a to z) or (A to Z)
# or (0 to 9). Characters that are not within a range can be
# matched by complementig the set. If the first character of
# the set is ^, all the characters that are not in the set will 
# be matched

re.search(r'Number: [0-6]', 'Number: 5').group()

# Matches any character except 5
re.search(r'Number: [^5]', 'Number: 0').group()

# \A - Uppercase a matches only at the start of the string
re.search(r'\A[A-E]ookie', 'Cookie')

# \b - Lowercase b matches only the beginning or end of the word
re.search(r'\b[A-Z]ookie', 'Cookie').group()

# \ - Backslash. If the character following the backslash is 
# recognized escape charactrer, then the special meaning of the
# term is taken. For example \n is considered as newline. However, 
# if the character following the \ is not a recognized escape 
# character, then the \ is treated like any other character and 
# passed through

# This checks for '\' in the string instead of '\t\ due to the
# '\' used
re.search(r'Back\\stail', 'Back\stail').group()

re.search(r'Back\stail','Back tail').group()



# The information gathered from this file was obtained from 
# https://www.datacamp.com/community/tutorials/python-regular-expression-tutorial?utm_source=adwords_ppc&utm_campaignid=1455363063&utm_adgroupid=65083631748&utm_device=c&utm_keyword=&utm_matchtype=b&utm_network=g&utm_adpostion=1t1&utm_creative=278443377077&utm_targetid=aud-392016246653:dsa-473406579035&utm_loc_interest_ms=&utm_loc_physical_ms=1010088&gclid=CjwKCAiA45njBRBwEiwASnZT59n_zHwAQTs3YgZt29NGi3nFiR4vRQHoLgVClp4GBE1CQ7H6kSEkXxoCbzgQAvD_BwE
# with the purpose of learning and practicing the basics 
# of regex in python for the following labs and activities 
# that will be done for the compilers lectures subject 

# ITESM GDL 2019 - ISC Adler Alonso Zamora Ruiz A01630908