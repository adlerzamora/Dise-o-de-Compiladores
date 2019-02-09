#!/usr/bin/env python
#Lab 2 Compilers Lecture Adler Zamora A01630908

f = open('hello.c', 'r')
stack = []
lastChar = ""
longComment = False
fail = False
singleQuote = False
doubleQuotes = False

for line in f:
    # print(line)
    if(not fail):
        lastChar = ""  # Resets slash counter for each new line
        for i in line:  # Checks if we have a fail
            if(not longComment and not singleQuote and not doubleQuotes):
                if i == "(" or i == "[" or i == "{":
                    stack.append(i)

                elif i == ")":  # looks for unbalanced parenthesis
                    if stack.pop() != "(" :
                        fail = True

                elif i == "}":  # looks for unbalanced braces
                    if stack.pop() != "{":
                        fail = True

                elif i == "]":  # looks for unbalanced brackets
                    if stack.pop() != "[":
                        fail = True

                elif i == "/":  # Detects line comments
                    if lastChar == "/":
                        lastChar = ""
                        break
                    else:
                        lastChar = "/"

                elif i == "*": # Detects start of long comment
                    if lastChar == "/":
                        longComment = True
                        lastChar = ""

                elif i == "'": # Detects single quotes
                    singleQuote = True

                elif i == '"': # Detects double quotes
                    doubleQuotes = True

            elif longComment:
                if i == "*": # Detects end of long comment
                    lastChar = "*"
                elif i == "/" and lastChar == "*":
                    lastChar = ""
                    longComment = False
            elif singleQuote:
                if i == ("'"):
                    singleQuote = False
            elif doubleQuotes:
                if i == ('"'):
                    doubleQuotes = False

f.close()  # closing read file


if longComment == True:
    print("LongComment never ended")
    fail = True
if singleQuote == True:
    print("SingleQuote never ended")
    fail = True
if doubleQuotes == True:
    print("DoubleQuotes never ended")
    fail = True

if fail:
    print("Syntax error, unbalance brackets, bracers or parenthesis")
    fail = True
else:
    print("Balanced")