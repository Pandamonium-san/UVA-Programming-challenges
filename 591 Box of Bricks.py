import sys

def main():
    #data = sys.stdin
    data = open(r"tests\591.txt", 'r')
    setNumber = 0
    while(True):
        n = int(data.readline())
        if(n == 0):
            return
        moves = 0
        setNumber += 1
        stacks = list(map(int, data.readline().split()))
        targetHeight = sum(stacks)/n
        for stack in stacks:
            if(stack>targetHeight):
                moves += int(stack - targetHeight)
        print("Set #{0}".format(setNumber))
        print("The minimum number of moves is {0}.".format(moves))
        print()
    return
main()
