import sys
import time

def DoTrading(town):
    balance = 0
    work = 0
    for a in town:
        work += abs(balance)
        balance += a
    return work

def main():
    #data = sys.stdin
    data = open(r"tests\11054.txt", 'r')
    result = ""
    while(True):
        size = int(data.readline())
        if(size == 0):
            break
        town = list(map(int, data.readline().split()))
        result += str(DoTrading(town)) + '\n'
    print(result, end="")
    return

start = time.clock()
main()
end = time.clock()
print('\n', end-start)
