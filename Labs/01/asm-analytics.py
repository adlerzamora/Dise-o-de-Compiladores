#!/usr/bin/env python
#Lab 1 Compilers Lecture Adler Zamora A01630908

assemblyDictionary={"aaa":0,"aad":0,"aam":0,"aas":0,"adc":0,"add":0,"and":0,"call":0,"callq":0,"cbw":0,"clc":0,"cld":0,"cli":0,"cmc":0,"cmp":0,"cmpb":0,"cmpq":0,"cmpsb":0,"cmpsw":0,"cvtss2sd":0,"cwd":0,"daa":0,"das":0,"dec":0,"div":0,"esc":0,"hlt":0,"idiv":0,"imul":0,"in":0,"inc":0,"int":0,"into":0,"iret":0,"jcc":0,"jcxz":0,"je":0,"jmp":0,"jmpq":0,"lahf":0,"lds":0,"lea":0,"leaveq":0,"les":0,"lock":0,"lodsb":0,"lodsw":0,"loop":0,"mov":0,"movb":0,"movd":0,"movsb":0,"movss":0,"movsw":0,"mul":0,"mulss":0,"neg":0,"nop":0,"nopl":0,"nopw":0,"not":0,"or":0,"out":0,"pop":0,"popf":0,"push":0,"pushf":0,"pushq":0,"rcl":0,"rcr":0,"rep":0,"repz":0,"ret":0,"retn":0,"retf":0,"retq":0,"rol":0,"ror":0,"sahf":0,"sal":0,"sar":0,"sbb":0,"scasb":0,"scasw":0,"shl":0,"shr":0,"stc":0,"std":0,"sti":0,"stosb":0,"stosw":0,"sub":0,"test":0,"wait":0,"xchg":0,"xlat":0,"xor":0}

f = open('logs', 'r')
functions = []
start = '<'
end ='>:'
instructionCounter = 0

for line in f:
    #Detects functions and 
    if ">:" in line:
        functions.append(line[line.find(start)+len(start):line.rfind(end)] + "  :  Located at " + line.split(' ',1)[0] + "addr")
    else:
        for assemCom in assemblyDictionary:
            if (assemCom+" ") in line:
                if assemblyDictionary[assemCom] == 0:
                    instructionCounter+=1
                assemblyDictionary[assemCom]+=1    

print("Lab 1 Compilers Lecture Adler Zamora A01630908\n\n")

print("Hi, this is the output of the analysis")

print("You have " + str(instructionCounter) + " kind of instructions in this object file:")
for assemInst in assemblyDictionary:
    if(assemblyDictionary[assemInst]>0):
        print(assemInst + "\t\t : Executed " + str(assemblyDictionary[assemInst]) + " times")
# Prints functions and their virtual address
print("\n\n You have " + str(len(functions)) + " functions:\n")
for function in functions:
    print(function)

