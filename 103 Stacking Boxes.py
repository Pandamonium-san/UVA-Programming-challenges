import sys
import time

#True if b1 is nested in b2
def isNestedIn(b1, b2):
    for i in range(len(b1) - 1): #don't check the identifier
        if(b1[i] >= b2[i]):
            return False
    return True

def LongestIncreasingSubsequence(boxlist):
    maxLength, bestEnd = 1, 0
    lisLengths = [1 for i in range(len(boxlist))]
    prev = [-1 for i in range(len(boxlist))]
    
    i, j = 1, 0
    while i < len(boxlist):
        j = 0
        while j < i:
            if(lisLengths[i] < lisLengths[j]+1 and
               isNestedIn(boxlist[j], boxlist[i])):
                lisLengths[i] = lisLengths[j] + 1
                prev[i] = j
            j += 1
        if(lisLengths[i] > maxLength):
            bestEnd = i
            maxLength = lisLengths[i]
        i += 1

    lis = []
    i = bestEnd
    while i != -1:
        lis.append(boxlist[i])
        i = prev[i]
    return lis

def Solve(k, n, data):
    boxbox = []
    for i in range(k):
        boxbox.append(list(map(int, data.readline().split())))
        boxbox[i].sort()
        boxbox[i].append(i+1) #add an identifier
    boxbox.sort()
    
    lis = LongestIncreasingSubsequence(boxbox)
    #print(lis[::-1])
    #print()
    
    #for box in boxbox:
    #    print(box)

    result = str(len(lis))+'\n'
    for box in lis[:0:-1]:
        #add identifier to result
        result += str(box.pop()) + ' '
    result += str(lis[0].pop())
    return result

def main():
    data = sys.stdin
    data = open(r"tests\103.txt", 'r')
    result = ""
    line = data.readline()
    while(line and line != '\n'):
        k, n = map(int, line.split())
        result += Solve(k, n, data) + '\n'
        line = data.readline()
        #print()
    print(result, end="")
    open(r"output.txt",'w').write(result)
    return
start = time.clock()
main()
end = time.clock()
print(end-start)
