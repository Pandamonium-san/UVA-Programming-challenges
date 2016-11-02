import sys
import functools
import time

@functools.lru_cache(None)
def CycleLength(n):
    if(n==1):
        return 1
    if(n % 2 == 0):
        n = n/2
    else:
        n = 3*n+1
    return CycleLength(n)+1

def main():
    testin = open(r"tests\100.txt", 'r')
    for line in testin:
        i, j = map(int, line.split())
        highest = 0
        for x in range(min(i,j), max(i,j)+1):
            highest = max(highest, CycleLength(x))
        print(i, j, highest)
    return
start = time.clock()
main()
end = time.clock()
print('\n'+str(end-start))

"""
import sys
import functools

@functools.lru_cache(None)
def CycleLength(n):
    if(n==1):
        return 1
    if(n % 2 == 0):
        n = n/2
    else:
        n = 3*n+1
    return CycleLength(n)+1

def main():
    for line in sys.stdin:
        i, j = map(int, line.split())
        highest = 0
        for x in range(min(i,j), max(i,j)+1):
            highest = max(highest, CycleLength(x))
        print(i, j, highest)
    return
main()
"""
