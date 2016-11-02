import sys
import operator
import time
from queue import Queue

class Graph:
    def __init__(self, data):
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
        self.visited = False
        self.neighbors = None
        self.set = self
        self.rank = 0
        if(char == '#'):
            self.blocked = True
        return
    
def Bfs(graph, root):
    frontier = Queue()
    frontier.put(root)
    cameFrom = {}
    cameFrom[root] = None

    while not frontier.empty():
        current = frontier.get()
        for next in graph.neighbors(current):
            if(next not in cameFrom and not next.blocked):
                frontier.put(next)
                cameFrom[next] = current
    return cameFrom

def PathLength(cameFrom, root, end):
    current = cameFrom[end]
    distance = 1
    while(current != root):
        current = cameFrom[current]
        distance += 1
    return distance

def Kruskal(distances):
    totalDistance = 0
    for n in distances:
        a = n[0][0]
        b = n[0][1]
        c = n[1]
        if(FindSet(a) != FindSet(b)):
            Union(a,b)
            totalDistance += c
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
    sCameFrom = Bfs(graph, graph.start)
    for a in graph.aliens:
        graph.distances[graph.start, a] = PathLength(sCameFrom, graph.start, a)
        aCameFrom = Bfs(graph, a)
        for b in graph.aliens:
            if(a != b and (b,a) not in graph.distances):
                graph.distances[(a, b)] = PathLength(aCameFrom, a, b)
    distances = sorted(graph.distances.items(), key=operator.itemgetter(1))
    print(Kruskal(distances))
    return

def main():
    #data = sys.stdin
    data = open(r"tests\10307.txt",'r')
    nrOfTestCases = int(data.readline())
    for i in range(nrOfTestCases):
        TestCase(data)
    return
start = time.time()
main()
end = time.time()
print(end-start)
