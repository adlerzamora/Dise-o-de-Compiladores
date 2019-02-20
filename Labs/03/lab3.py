#!/usr/bin/env python
# Lab 3 Compilers Lecture Adler Zamora A01630908

f = open('lex.ac', 'r') #file where our source code is being readed
g = open("lex.out", "a") #file where our target code is being written

fail = False  # depracated variables

fDef = False
iDef = False
pDef = False
asignDef = False
addDef = False

currentLine = ''

currentToken = ''
lastToken = ''
tokenDictionary = []

for line in f:
    if(not fail): # Depracated if
        for i in line:
            if(len(currentToken) == 2 and currentToken == '//'):
                # print('Comment detected') # Detects // comments as in the example lex.ac s
                currentToken = ''
                break
            elif(not(i.isspace())):
                if(i == '='):
                    asignDef = True
                    currentLine += 'asign '
                    currentToken = ''
                elif(i == '+'):
                    addDef = True
                    currentLine += 'plus '
                    currentToken = ''
                else:
                    currentToken += str(i)
            elif(i.isspace()):
                if(currentToken == 'f'):
                    fDef = True
                    currentLine += 'floatdcl '
                    currentToken = ''
                elif(currentToken == 'i'):
                    iDef = True
                    currentLine += 'intdcl '
                    currentToken = ''
                elif(currentToken == 'p'):
                    currentLine += 'print '
                    currentToken = ''
                else:
                    if(currentToken != '' and not(currentToken.isspace())):
                        if(currentToken in tokenDictionary):
                            # print('token allready in list: ' + currentToken) #token is allready in list
                            currentLine += 'id '
                        else:
                            tokenDictionary.append(currentToken) #new Token added
                            try:
                                int(currentToken)
                                currentLine += 'inum '
                            except ValueError:
                                try:
                                    float(currentToken)
                                    currentLine += 'fnum '
                                except ValueError:
                                    currentLine += 'id '
                            # if(fDef):
                            #    #print('token: ' + currentToken + ' added as a float')
                            #    tokenDictionary.append(currentToken) #new Token added
                            #    currentLine += 'id '
                            #    fDef = False
                            # elif(iDef):
                            #    #print('token: ' + currentToken + ' added as an int')
                            #    tokenDictionary.append(currentToken) #new Token added
                            #    currentLine += 'id '
                            #    iDef=False
                            # else:
                            #    #print('definition not identified:' + lastToken)
                            #    tokenDictionary.append(currentToken)
                            #    currentLine +='id '
                            currentToken = ''
                        if(currentToken!=''):
                            lastToken=currentToken
        if(currentLine != ''):
            print(currentLine)
            g.write(currentLine+'\n')
        currentLine=''
        # to do after a line is read

# Quickfix - Not recommended

if(currentToken=='='):
    g.write('assing ')
elif(currentToken=='+'):
    g.write('plus ')
elif(currentToken == 'f'):
    g.write('floatdcl ')
elif(currentToken == 'i'):
    g.write('intdcl ')
elif(currentToken == 'p'):
    g.write('print ')
else:
    try:
        int(currentToken)
        g.write('inum ')
    except ValueError:
        try:
            float(currentToken)
            g.write('fnum ')
        except ValueError:
            g.write('id ')

# Quickfix end

f.close()  # closing read file  
g.close()
#print(tokenDictionary)
