import sys
import time
import re

'''
I 0 1 2 3 4 5 6 7 8 9
V 0 1 2 3 4 5 6 7 8 9
X 0 1 2 3 4 5 6 7 8 9
L 0 1 2 3 4 5 6 7 8 9
C 0 1 2 3 4 5 6 7 8 9
D 0 1 2 3 4 5 6 7 8 9
M 0 1 2 3 4 5 6 7 8 9

I+XXI=XCV ambiguous
X+XII=MCC valid

M=1, V=9, I+I != x9
XVI+VII=MXIV impossible

last digit of A + last digit of B determines last digit of C

cases assuming previous does not add 1:
__X + __X = __X valid, X = 0, can not add 1
__Y + __X = __X ambiguous, Y = 0, can not add 1
__X + __X = __Y ambiguous, can add 1, Y = 0,2,4,6,8 <-- may conflict with other
__X + __Y = __Z ambiguous, can add 1

digit i of A + digit i of B determines digit i of C and possibly i+1

cases assuming i-1 adds 1 to C[i]:
_X_ + _X_ = _X_ X = 9, valid, adds 1, previous must add 1
_Y_ + _X_ = _X_ Y = 9, ambiguous, adds 1, previous must add 1
_X_ + _X_ = _Y_ ambiguous, can add 1
_X_ + _Y_ = _Z_ ambiguous, can add 1

A or B has fewer letters:
(ab)  (c)
_X_ = _X_ ambiguous, can not add 1, previous does not add 1
_X_ = _Y_ ambiguous, can add 1, if add 1: X=9 Y=0, previous must add 1, Y = X+1

if(add1):
    if b[i] == c[i]
        return "impossible"
if(canAdd1):
    proceed
then check for each letter
if(b[i] != c[i]):
    return "impossible"
    
C length = longest+1:
first of C must be 1
second has to add 1

longest = max(len(a), len(b))
if(len(c) < longest or len(c) > longest+1):
    return "impossible"
'''
rom = {'I':1,
         'V':5,
         'X':10,
         'L':50,
         'C':100,
         'D':500,
         'M':1000}
cPoss = {}
cVal = {}
split = []
index = 0
add1 = False
solutions = 0
stop = False

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

def IsValidEncoding(a, b, c):
    global index, add1, cPoss, solutions, stop
    solutions = 0
    stop = False
    index = 0
    add1 = False
    cPoss = {}
    alen, blen, clen = len(a), len(b), len(c)
    
    #put longest in b
    #if(alen > blen):
    #    a, b = b, a
    #    alen, blen = blen, alen

    #return if clen impossible length
    if(clen < blen or clen > blen+1):
        return "impossible"
    
    #make a and b same length as c
    #a = (" " * (clen - alen)) + a
    #b = (" " * (clen - blen)) + b

    #c[0] has to be 1 if clen > blen
    if(clen == blen+1):
        cPoss[c[0]] = [1]
        #index += 1
        #add1 = True

    #loop through and check validity
    #print(index, clen)
    #while(index < clen):
    #    if(not CheckValid(a, b, c, index)):
    #        return "impossible"
    #    index += 1
    
    for A in a:
        if A not in cPoss:
            cPoss[A] = [x for x in range(10)]
    for B in b:
        if B not in cPoss:
            cPoss[B] = [x for x in range(10)]
    for C in c:
        if C not in cPoss:
            cPoss[C] = [x for x in range(10)]
            
    #print(cPoss)
    #if(add1):
    #    return "impossible"
    
    forloop(list(cPoss.keys()), 0)
    #print(solutions)
    if(solutions == 1):
        return "valid"
    if(solutions == 0):
        return "impossible"
    return "ambiguous"

def forloop(keys, depth):
    global split, solutions, stop
    if(stop):
        return
    if(depth < len(keys)):
        for x in cPoss[keys[depth]]:
            cVal[keys[depth]] = x
            forloop(keys, depth+1)
    else:
        n1 = toNumber(split[0])
        n2 = toNumber(split[1])
        n3 = toNumber(split[2])
        #print(n1,n2,n3)
        if(n1 == 0 and n2 == 0 and n3 == 0):
            return
        if(n1 + n2 == n3):
            solutions += 1
            if(solutions == 2):
                stop = True
    return

def toNumber(string):
    num = cVal[string[0]]
    for c in string[1::]:
        num = num * 10 + cVal[c]
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
            if(add1):
                for i in range(10)[5::]:
                        cPoss[C] = RemoveValue(cPoss[C], i)
                        cPoss[B] = RemoveValue(cPoss[B], i)
            add1 = False
        else:
            if(add1):
                cPoss[B] = RemoveAllExceptValue(cPoss[B], 9)
                cPoss[C] = RemoveAllExceptValue(cPoss[C], 0)
            else:
                cPoss[C] = [x for x in cPoss[C] for y in cPoss[B] if x==y+1]
            add1 = True
        #_X_ = _X_ ambiguous, can not add 1, previous can not add 1
        #_X_ = _Y_ ambiguous, can add 1, if add 1: X=9 Y=0, previous must add 1, Y = X+1
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
            else:
                if(add1):
                    for i in range(5):
                        cPoss[A] = RemoveValue(cPoss[A], i)
                        cPoss[B] = RemoveValue(cPoss[B], i)
                cPoss[C] = [x for x in cPoss[C] for y in cPoss[A] if x==y*2%10]
                add1 = False
        elif(A != B):
            if(add1):
                if(A==C):
                    cPoss[A] = RemoveAllExceptValue(cPoss[A], 9)
                elif(B==C):
                    cPoss[B] = RemoveAllExceptValue(cPoss[B], 9)
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
    return True

def RemoveValue(list, value):
    try:
        list.remove(value)
    except ValueError:
        pass
    return list

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
    print(result,end='')
    return
start = time.clock()
main()
end = time.clock()
print(end-start)
