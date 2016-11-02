import sys
import time

def IsSubsequence(s, t):
    sLen = len(s)
    j = 0
    for i in range(len(t)):
        if(s[j] == t[i]):
            j += 1
            if(j == sLen):
                return True
    return False

def main():
    data = sys.stdin
    data = open(r"tests\10340.txt", 'r')
    currLine = data.readline()
    while(currLine):
        s, t = currLine.split()
        if(IsSubsequence(s,t)):
            print("Yes")
        else:
            print("No")
        currLine = data.readline()
    return
start = time.time()
main()
end = time.time()
print(end-start)
