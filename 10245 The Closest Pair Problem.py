import sys
import time
import math

def dis(p1, p2):
    return dsq(p1, p2)**0.5
def dsq(p1, p2):
    return (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2

def trivialcp(P):
    min = math.inf
    for i in P:
        for j in P:
            if(i==j):
                continue
            if(dsq(i,j) < min):
                min = dsq(i,j)
    return min**0.5

def cp(P):
    if(len(P) < 4):
        return trivialcp(P)
    
    L = P[:len(P)//2]
    R = P[len(P)//2:]
    vline = R[0][0]
    d = min(cp(L), cp(R))
    
    L = [p for p in L if vline - p[0] < d]
    R = [p for p in R if p[0] - vline < d]
    L.sort(key=lambda x: x[1])
    R.sort(key=lambda x: x[1])
    
    for p1 in L:
        for p2 in R:
            if(abs(p1[1] - p2[1]) < d and dis(p1, p2) < d):
                d = dis(p1, p2)
    return d

def main():
    data = sys.stdin
    data = open(r"tests\10245.txt.",'r')
    N = int(data.readline())
    while(N != 0):
        P = []
        for i in range(N):
            p = list(map(float, data.readline().split()))
            P.append(p)
        P.sort()
        d = cp(P)
        if(d < 10000):
            print("%.4f" %d)
        else:
            print("INFINITY")
        N = int(data.readline())
    return
start = time.clock()
main()
end = time.clock()
print(end-start)
