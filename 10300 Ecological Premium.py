import sys

def main():
    f = open(r"tests\10300.txt",'r')
    testCases = f.readline()
    if testCases is '\n':
        testCases = f.readline()
    testCases = int(testCases)
    #testCases = stdin.readline()
    for x in range(0, testCases):
        #farmers = stdin.readline()
        farmers = int(f.readline())
        premium = 0
        for y in range(0, farmers):
            #line = stdin.readline()
            line = f.readline()
            size, animals, env = map(int, line.split())
            #premium += (size/animals) * env * animals
            premium += size * env
        print(int(premium))
    return
main()

"""
import sys

def main():
    testCases = int(sys.stdin.readline())
    for x in range(0, testCases):
        farmers = int(sys.stdin.readline())
        premium = 0
        for y in range(0, farmers):
            line = sys.stdin.readline()
            size, animals, env = map(int, line.split(' '))
            premium += size * env
        print(int(premium))
    return
main()
"""
