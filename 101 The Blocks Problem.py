import sys
import time
        
class Block():
    below = None
    above = None
    stack = -1
    def __init__(self, stack):
        self.stack = stack
        self.id = stack
        return

blocks = {}

def moveOnto(A, B):
    if(A.below):
        A.below.above = None
    InitAbove(A)
    InitAbove(B)
    A.below = B
    B.above = A
    A.stack = B.stack
    return
def moveOver(A, B):
    if(A.below):
        A.below.above = None
    InitAbove(A)
    bTop = GetTop(B)
    bTop.above = A
    A.below = bTop
    A.stack = B.stack
    return
def pileOnto(A, B):
    if(A.below):
        A.below.above = None
    InitAbove(B)
    B.above = A
    A.below = B
    aTop = A
    while(aTop != None):
        aTop.stack = B.stack
        aTop = aTop.above
    return
def pileOver(A, B):
    if(A.below):
        A.below.above = None
    bTop = GetTop(B)
    bTop.above = A
    A.below = bTop
    aTop = A
    while(aTop != None):
        aTop.stack = B.stack
        aTop = aTop.above
    return

def GetTop(block):
    top = block
    while(top.above != None):
        top = top.above
    return top
def Init(block):
    block.stack = block.id
    block.above = None
    block.below = None
    return
def InitAbove(block):
    bTop = block.above
    while(bTop != None):
        if(bTop.above == None):
            Init(bTop)
            break
        bTop = bTop.above
        Init(bTop.below)
    block.above = None
    return

def ProcessCommand(line):
    w1, a, w2, b = line.split()
    A, B = blocks[int(a)], blocks[int(b)]
    
    if(A == B or A.stack == B.stack):
        return
    
    if(w1 == "move"):
        if(w2 == "over"):
            moveOver(A, B)
        elif(w2 == "onto"):
            moveOnto(A, B)
    elif(w1 == "pile"):
        if(w2 == "over"):
            pileOver(A, B)
        elif(w2 == "onto"):
            pileOnto(A, B)
    return

def PrintStacks(n):
    result = ""
    for i in range(n):
        if(i != 0):
            result += "\n"
        result += str(i) + ":"
        if(blocks[i].stack == i):
            result += " " + str(i)
            top = blocks[i].above
            while(top != None):
                result += " " + str(top.id) #+ "("+str(top.stack)+")"
                top = top.above
    print(result)
    return

def main():
    data = sys.stdin
    data = open(r"tests\101.txt", 'r')
    n = int(data.readline())
    for i in range(n):
        blocks[i] = Block(i)
    line = data.readline()
    while(line != "quit" and line != "quit\n"):
        ProcessCommand(line)
        line = data.readline()
    PrintStacks(n)
    return
start = time.clock()
main()
end = time.clock()
print(end-start)
