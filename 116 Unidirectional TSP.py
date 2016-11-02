import sys
import time
import math

class Graph:
    def __init__(self, dataitr, h, w):
        self.h, self.w = h, w
        self.nodes = [['' for x in range(self.w)] for y in range(self.h)]
        for y in range(self.h):
            for x in range(self.w):
                self.nodes[y][x] = Node(next(dataitr, ''), x, y)
        return
    def neighbors(self, n):
        #if(n.neighbors is not None):
        #    return n.neighbors
        result = []
        if n.x+1 < self.w:
            if n.y-1 >= 0:
                result.append(self.nodes[n.y-1][n.x+1])
            else:
                result.append(self.nodes[self.h-1][n.x+1])
            if n.x+1 < self.w:
                result.append(self.nodes[n.y][n.x+1])
            if n.y+1 < self.h:
                result.append(self.nodes[n.y+1][n.x+1])
            else:
                result.append(self.nodes[0][n.x+1])
        #n.neighbors = result
        return result
    
class Node:
    def __init__(self, weight, x, y):
        self.x = x
        self.y = y
        self.weight = weight
        self.distance = math.inf
        #self.neighbors = None
        self.link = None
        return
    
def Update(current, n):
    if(n.distance + current.weight <= current.distance):
        current.distance = n.distance + current.weight
        current.link = n
    elif(n.distance + current.weight == current.distance):
        if(n.y < current.link.y):
           current.link = n
    return current.distance

def GetPath(n):
    path = []
    while(n != None):
        path.append(n.y+1)
        n = n.link
    return path

def SolveTSP(graph):
    #Loop through graph and update distance
    for i in range(graph.w-1, -1, -1):
        for j in range(graph.h):
            current = graph.nodes[j][i]
            neighbors = graph.neighbors(current)
            if(len(neighbors) > 0):
                for n in neighbors:
                    Update(current, n)
            else:
                current.distance = current.weight
                
    #Find lowest weight
    lowest = math.inf
    index = 0
    for j in range(graph.h):
        if(graph.nodes[j][0].distance < lowest):
            lowest = graph.nodes[j][0].distance
            index = j
    
    #Traceback path        
    path = GetPath(graph.nodes[index][0])
    
    #Build result string
    result = ""
    result += str(path[0])
    for i in path[1::]:
        result += ' ' + str(i)
    result += '\n' + str(lowest)
    return result

def ReadInput(data):
    dataitr = list(data.read().split())
    dataitr = iter([int(c) for c in dataitr])
    return dataitr

def main():
    data = sys.stdin
    data = open(r"tests\116.txt")
    dataitr = ReadInput(data)
    
    result = ""
    h = next(dataitr, '')
    while(h != ''):
        w = next(dataitr, '')
        graph = Graph(dataitr, h, w)
        result += SolveTSP(graph)+'\n'
        h = next(dataitr, '') 
    print(result, end='')
    
    return
start = time.clock()
main()
end = time.clock()
print(end-start)
