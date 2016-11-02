import sys
import time
import re

rom = {'I':1,
         'V':5,
         'X':10,
         'L':50,
         'C':100,
         'D':500,
         'M':1000}

def to_arabic(s):
    result = 0
    x = 0
    while x < len(s):
        if(x == len(s)-1 or rom[s[x]] >= rom[s[x+1]]):
            result += rom[s[x]]
        else:
            result += rom[s[x+1]] - rom[s[x]]
            x += 1
        x += 1
    return result
                   
def IsValidRoman(a, b, c):
    a = to_arabic(a)
    b = to_arabic(b)
    c = to_arabic(c)

    if(a + b == c):
        return "Correct"
    else:
        return "Incorrect"

cPoss = {}
cVal = {}
cKey = {}
index = 0
add1 = False
def IsValidEncoding(a, b, c):
    global index, add1, cPoss, solutions, stop, cKey, cVal
    solutions = 0
    stop = False
    index = 0
    add1 = False
    cPoss = {}
    cVal = {}
    cKey = {}
    alen, blen, clen = len(a), len(b), len(c)
    
    #put longest in b
    if(alen > blen):
        a, b = b, a
        alen, blen = blen, alen

    #return if clen impossible length
    if(clen < blen or clen > blen+1):
        return "impossible"
    
    #make a and b same length as c
    a = (" " * (clen - alen)) + a
    b = (" " * (clen - blen)) + b

    #c[0] has to be 1 if clen > blen
    if(clen == blen+1):
        cPoss[c[0]] = [1]
        index += 1
        add1 = True

    #loop through and check validity
    while(index < clen):
        CheckValid(a, b, c, index)
        index += 1
    
    #print(cPoss)
    if(add1):
        return "impossible"

    #bruteforce remaining possibilities using recursive looping
    myl = list(cPoss.keys())
    myl.sort()
    forloop(myl, 0)
    
    #print(solutions)
    if(solutions == 1):
        return "valid"
    if(solutions == 0):
        return "impossible"
    
    return "ambiguous"

split = []
solutions = 0
stop = False
def forloop(keys, depth):
    global split, solutions, stop
    if(stop):
        return
    if(depth < len(keys)):
        for x in cPoss[keys[depth]]:
            if(x in cKey and cKey[x] == 1):
                continue
            cKey[x] = 1
            cVal[keys[depth]] = x
            forloop(keys, depth+1)
            cKey[x] = 0
    else:
        n1 = toNumber(split[0])
        n2 = toNumber(split[1])
        n3 = toNumber(split[2])
        if(n1 == 0 or n2 == 0 or n3 == 0):
            return
        #print(n1,n2,n3)
        if(n1 + n2 == n3):
            solutions += 1
            #print("C")
            if(solutions == 2):
                stop = True
    return

def toNumber(string):
    if(cVal[string[0]] == 0):
        return 0
    num = 0
    for c in string:
        num = num * 10 + cVal[c]
    #print(string, num)
    return num

def CheckValid(a, b, c, index):
    global add1, cPoss
    A = a[index]
    B = b[index]
    C = c[index]
    
    if(A not in cPoss and A != " "):
        cPoss[A] = [x for x in range(10)]
    if(B not in cPoss):
        cPoss[B] = [x for x in range(10)]
    if(C not in cPoss):
        cPoss[C] = [x for x in range(10)]
    #print(A,B,C)

    if(A==" "):
        if(B == C):
            add1 = False
        else:
            if(add1):
                cPoss[B] = RemoveAllExceptValue(cPoss[B], 9)
                cPoss[C] = RemoveAllExceptValue(cPoss[C], 0)
            add1 = True
        #_X_ = _X_ ambiguous, can add 1, next can not add 1
        #_X_ = _Y_ ambiguous, can add 1, if add 1: X=9 Y=0, next must add 1, Y = X+1
    else:
        if(A==B):
            if(A==C):
                if(add1):
                    cPoss[A] = RemoveAllExceptValue(cPoss[A], 9)
                    cPoss[B] = RemoveAllExceptValue(cPoss[B], 9)
                    cPoss[C] = RemoveAllExceptValue(cPoss[C], 9)
                    add1 = True
                else:
                    cPoss[A] = RemoveAllExceptValue(cPoss[A], 0)
                    cPoss[B] = RemoveAllExceptValue(cPoss[B], 0)
                    cPoss[C] = RemoveAllExceptValue(cPoss[C], 0)
                    add1 = False
            #A==B!=C
            else:
                add1 = False
        elif(A != B):
            if(add1):
                if(A==C):
                    cPoss[B] = RemoveAllExceptValue(cPoss[B], 9)
                elif(B==C):
                    cPoss[A] = RemoveAllExceptValue(cPoss[A], 9)
                else:
                    add1 = False
            else:
                if(A==C):
                    cPoss[B] = RemoveAllExceptValue(cPoss[B], 0)
                elif(B==C):
                    cPoss[A] = RemoveAllExceptValue(cPoss[A], 0)
                #else: #A!=B!=C
                add1 = False
                
#cases assuming previous does not add 1:
#__X + __X = __X valid, X = 0, can not add 1
#__Y + __X = __X ambiguous, Y = 0, can not add 1
#__X + __X = __Y ambiguous, can add 1, Y = 0,2,4,6,8
#__X + __Y = __Z ambiguous, can add 1

#cases assuming i-1 adds 1 to C[i]:
#_X_ + _X_ = _X_ X = 9, valid, adds 1, previous must add 1
#_Y_ + _X_ = _X_ Y = 9, ambiguous, adds 1, previous must add 1
#_X_ + _X_ = _Y_ ambiguous, can add 1, Y = 0,2,4,6,8
#_X_ + _Y_ = _Z_ ambiguous, can add 1
    return

def RemoveAllExceptValue(list, value):
    return [x for x in list if x == value]

def main():
    global split
    data = sys.stdin
    data = open(r"tests\185.txt",'r')
    line = data.readline()
    result = ""
    while(line != "#\n" and line != "#"):
        split = re.split('\+|\=|\n', line)
        result += IsValidRoman(split[0],split[1],split[2]) + ' '
        result += IsValidEncoding(split[0],split[1],split[2]) + '\n'
        line = data.readline()
    print(result, end='')
    return
start = time.clock()
main()
end = time.clock()
print(end-start)
