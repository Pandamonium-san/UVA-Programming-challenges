import sys
import time
import math

char = ['B','G','C']
order = [0, 2, 1]

def GetVal(a, b, c, data):
    sum = 0
    for i in range(len(data)):
        if i != a and i != b+3 and i != c+6:
            sum += data[i]
    return sum

def Solve(inData):
    minCost = math.inf
    minStr = ""
    for x in order:
        for y in order:
            if(y == x):
                continue
            for z in order:
                if(z == y or z == x):
                    continue
                cost = GetVal(x, y, z, inData)
                if(cost < minCost):
                    minCost = cost
                    minStr = char[x] + char[y] + char[z]
    return minStr + ' ' + str(minCost)

def main():
    data = sys.stdin
    data = open(r"tests\102.txt", 'r')
    inData = list(map(int, data.readline().split()))
    result = ""
    while(inData):
        result += Solve(inData) + '\n'
        inData = list(map(int, data.readline().split()))
    print(result, end="")
    return
start = time.clock()
main()
end = time.clock()
print(end-start)
