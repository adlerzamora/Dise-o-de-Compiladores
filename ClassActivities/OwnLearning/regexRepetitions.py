import re

# It becomes quite tedious if you are looking to find long patterns
# in a sequence. Fortunately, the re module handles repetitions using
# the following special characters:

# + - Checks for one or more characters to its left
re.search(r'Co+kie','Cooookie').group()

# * - Checks for zero or more characters to its left
re.search(r'Ca*o*kie','Caaaaooooookie').group()

# ?  - Checks for exactly zero or one character to its lef
re.search(r'Colou?r','Color').group()

# If you want to check for exact number of sequence repetitions,
# for example, the validity of a phone number in an application...

# {x} - Repeat exactly x number of times
# {x,} - Repeat at least x times or more
# {x, y} - Repeat at least x times but no more than y times
re.search(r'\d{9,10}','3112004870').group()

# The + and * qualifiers are said to be greedy.

# The information gathered from this file was obtained from 
# https://www.datacamp.com/community/tutorials/python-regular-expression-tutorial?utm_source=adwords_ppc&utm_campaignid=1455363063&utm_adgroupid=65083631748&utm_device=c&utm_keyword=&utm_matchtype=b&utm_network=g&utm_adpostion=1t1&utm_creative=278443377077&utm_targetid=aud-392016246653:dsa-473406579035&utm_loc_interest_ms=&utm_loc_physical_ms=1010088&gclid=CjwKCAiA45njBRBwEiwASnZT59n_zHwAQTs3YgZt29NGi3nFiR4vRQHoLgVClp4GBE1CQ7H6kSEkXxoCbzgQAvD_BwE
# with the purpose of learning and practicing the basics 
# of regex in python for the following labs and activities 
# that will be done for the compilers lectures subject 

# ITESM GDL 2019 - ISC Adler Alonso Zamora Ruiz A01630908