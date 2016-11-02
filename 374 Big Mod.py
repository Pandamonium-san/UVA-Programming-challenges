import sys
import time

def modexp(x,y,m):
    if(m == 1):
        return 0
    if(y == 0):
        return 1
    x1 = x % m
    p = 1
    while y > 0:
        if y % 2 == 1:
            p *= x1
            p = p % m
            y -= 1
        y /= 2
        x1 = (x1*x1)%m
    return p

def main():
    #data = sys.stdin
    data = list(open(r"tests\374.txt", 'r'))
    result = ""
    for i in range(0, len(data), 4):
        b = int(data[i])
        p = int(data[i+1])
        m = int(data[i+2])
        result += str(modexp(b,p,m))+'\n'
        #print(modexp(b,p,m))
    print(result)
    return
start = time.clock()
main()
end = time.clock()
print(end-start)
