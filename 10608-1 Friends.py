import sys
import time

class Node:
    def __init__(self, id):
        self.id = id
        self.friends = {}
        self.visited = False

def DFS(graph):
    stack = []
    biggest = 0
    for v in graph:
        if(v.visited):
            continue
        componentSize = 0
        stack.append(v)
        while(stack):
            current = stack.pop()
            current.visited = True
            for u in current.friends:
                if(not graph[u].visited and
                   not graph[u] in stack):
                    stack.append(graph[u])
            componentSize += 1
        biggest = max(biggest, componentSize)
    if(biggest == 1):
        biggest = 0
    return biggest

def TestCase(data):
    graph = []
    n, m = map(int, data.readline().split())
    for i in range(n):
        graph.append(Node(i))
    for i in range(m):
        a, b = map(int, data.readline().split())
        graph[a-1].friends[b-1] = True
        graph[b-1].friends[a-1] = True
    return DFS(graph)

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

