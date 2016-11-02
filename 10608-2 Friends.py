import sys
import time

class Node:
    def __init__(self, id):
        self.parent = self
        self.id = id
        self.size = 1
        self.rank = 0
    def SetParent(self, parent):
        self.parent = parent
        parent.size += self.size
        if(self.rank == parent.rank):
            parent.rank += 1

def FindSet(v):
    if(v.parent == v):
        return v
    else:
        return FindSet(v.parent)

def Union(u, v):
    uRoot = FindSet(u)
    vRoot = FindSet(v)
    if(uRoot == vRoot):
        return 0
    if(uRoot.rank < vRoot.rank):
        uRoot.SetParent(vRoot)
        return vRoot.size
    else:
        vRoot.SetParent(uRoot)
        return uRoot.size
    

def TestCase(data):
    nodes = []
    biggest = 0
    n, m = map(int, data.readline().split())
    for i in range(n):
        nodes.append(Node(i))
    for i in range(m):
        a, b = map(int, data.readline().split())
        biggest = max(biggest, Union(nodes[a-1], nodes[b-1]))
    if(biggest == 1):
        biggest = 0
    return biggest

def main():
    #data = sys.stdin
    data = open(r"tests\10608.txt", 'r')
    result = ""
    nrOfTestCases = int(data.readline())
    for i in range(nrOfTestCases):
        result += str(TestCase(data)) + '\n'
    print(result)
    return
start = time.clock()
main()
end = time.clock()
print(end-start)
