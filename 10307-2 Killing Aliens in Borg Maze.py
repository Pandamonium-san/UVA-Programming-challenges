import sys
import operator
import time
from queue import Queue

class Graph:
    def __init__(self, data):
        clock = 1
        self.aliens = []
        self.distances = {}
        self.start = Node('S',0,0)
        self.w, self.h = map(int, data.readline().split())
        self.nodes = [[' ' for x in range(self.w)] for y in range(self.h)]
        for y in range(self.h):
            currLine = data.readline()
            for x in range(self.w):
                self.nodes[y][x] = Node(currLine[x],x,y)
                if(currLine[x] == 'S'):
                    self.start = self.nodes[y][x]
                elif(currLine[x] == 'A'):
                    self.aliens.append(self.nodes[y][x])
        return
    def neighbors(self, n):
        if(n.neighbors is not None):
            return n.neighbors
        result = []
        if n.y+1 < self.h:
            result.append(self.nodes[n.y+1][n.x])
        if n.y-1 > 0:
            result.append(self.nodes[n.y-1][n.x])
        if n.x+1 < self.w:
            result.append(self.nodes[n.y][n.x+1])
        if n.x-1 > 0:
            result.append(self.nodes[n.y][n.x-1])
        n.neighbors = result
        return result

class Node:
    blocked = False
    def __init__(self, char, x, y):
        self.x = x
        self.y = y
        self.char = char
        self.explored = False
        self.neighbors = None
        self.set = self
        self.rank = 0
        if(char == '#'):
            self.blocked = True
        return
    
def Bfs(graph, start):
    aCount = 0
    frontier = Queue()
    frontier.put(start)
    distances = {}
    distances[start] = 0
    while not frontier.empty():
        current = frontier.get()
        if(current.explored):
            return
        for next in graph.neighbors(current):
            if(next not in distances and not next.blocked):
                frontier.put(next)
                distances[next] = distances[current]+1
        if(current.char == 'A'):
            graph.distances[(start, current)] = distances[current]
            aCount += 1
            if(aCount == 20):
                return
    start.explored = True
    return distances

def Kruskal(distances, maxCount):
    distances = sorted(distances.items(), key=operator.itemgetter(1))
    count = 1
    totalDistance = 0
    for n in distances:
        a = n[0][0]
        b = n[0][1]
        c = n[1]
        #print(a.char,b.char,c)
        if(FindSet(a) != FindSet(b)):
            Union(a,b)
            totalDistance += c
            count += 1
            if(count == maxCount):
                break;
    return totalDistance

def FindSet(v):
    if(v.set == v):
        return v
    else:
        return FindSet(v.set)

def Union(u, v):
    uRoot = FindSet(u)
    vRoot = FindSet(v)
    if(uRoot == vRoot):
        return
    if(uRoot.rank < vRoot.rank):
        uRoot.set = vRoot
    elif(uRoot.rank > vRoot.rank):
        vRoot.set = uRoot
    else:
        vRoot.set = uRoot
        uRoot.rank += 1

def TestCase(data):
    graph = Graph(data)
    Bfs(graph, graph.start)
    for a in graph.aliens:
        Bfs(graph, a)
    mstSize = Kruskal(graph.distances, len(graph.aliens)+1)

    return mstSize

def main():
    #data = sys.stdin
    data = open(r"tests\10307-1.txt",'r')
    result = ""
    nrOfTestCases = int(data.readline())
    for i in range(nrOfTestCases):
        result += str(TestCase(data))+'\n'
    print(result, end="")
    return
start = time.time()
main()
end = time.time()
print(end-start)
