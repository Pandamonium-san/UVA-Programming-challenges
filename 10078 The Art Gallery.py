import sys
import time

def cross(u, v):
    return u[0] * v[1] - u[1] * v[0]

def IsLeft(p1 ,p2, p3):
    u = p2[0] - p1[0], p2[1] - p1[1]
    v = p3[0] - p2[0], p3[1] - p2[1]
    return cross(u,v) > 0

def IsConvex(points, N):
    isLeft = IsLeft(points[0], points[1], points[2])
    for i in range(N)[1::]:
        if(IsLeft(points[i], points[(i+1)%N], points[(i+2)%N]) != isLeft):
            return "Yes"
    return "No"

def main():
    data = sys.stdin
    data = open(r"tests\10078.txt.",'r')
    N = int(data.readline())
    while(N != 0):
        points = []
        for i in range(N):
            point = list(map(int, data.readline().split()))
            points.append(point)
        print(IsConvex(points, N))
        N = int(data.readline())
    return
start = time.clock()
main()
end = time.clock()
print(end-start)
