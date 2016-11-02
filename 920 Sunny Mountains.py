import sys
import time
import math

class Vector:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __lt__(self, other):
        return self.x < other.x
    def __add__(self, other):
        return Vector(self.x+other.x,self.y+other.y)
    def __sub__(self, other):
        return Vector(self.x-other.x,self.y-other.y)
    def __mul__(self, value):
        return Vector(self.x * value, self.y * value)
    def Length(self):
        return math.sqrt(math.pow(self.x, 2)+math.pow(self.y, 2))
    
def Dot(v1, v2):
    return (v1.x * v2.x + v1.y + v2.y)
def GetLength(p1, p2):
    P = p2 - p1
    return P.Length()

def Solve(data):
    points = []
    n = int(data.readline())
    for i in range(n):
        x, y = map(int, data.readline().split())
        p = Vector(-x, y)   #reverse sorted list
        points.append(p)
    points.sort()
    
    height = 0
    total = 0
    for i in range(len(points))[1::2]:
        if(points[i].y < height):
            continue
        #calculate congruent triangles
        #large
        T_height = points[i].y - points[i-1].y
        T_hypo = GetLength(points[i], points[i-1])
        #small
        t_height = points[i].y - height
        t_hypo = (T_hypo*t_height)/T_height
        print(T_height,T_hypo,t_height)
        total += t_hypo
        height = points[i].y
    return total

def main():
    data = sys.stdin
    data = open(r"tests\920.txt", 'r')
    testCases = int(data.readline())
    for i in range(testCases):
        print("%.2f" %Solve(data))
    return
start = time.clock()
main()
end = time.clock()
print(end-start)
