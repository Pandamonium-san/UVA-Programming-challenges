import sys
import time

class Group():
    def __init__(self, citizen):
        self.people = []
        self.Append(citizen)
    def Assimilate(self, other):
        if(self == other):
            return
        self.people = self.people + other.people
        for c in other.people:
            c.group = self
        return
    def Append(self, citizen):
        citizen.group = self
        self.people.append(citizen)
        return
    def Size(self):
        return len(self.people)
class Citizen():
    group = None
    def HasGroup(self):
        return self.group is not None

def FindFriends(citizen, friend):
    if(citizen == friend):
        return 0
    
    f = friend.HasGroup()
    c = citizen.HasGroup()
    
    if(not c and not f):
        Group(citizen)
        citizen.group.Append(friend)
    elif(c and not f):
        citizen.group.Append(friend)
    elif(f and not c):
        friend.group.Append(citizen)
    elif(f and c):
        citizen.group.Assimilate(friend.group)
        
    return citizen.group.Size()

def main():
    #data = sys.stdin
    data = open(r"tests\10608.txt", 'r')
    nrOfTestCases = int(data.readline())
    result = ""
    for x in range(0, nrOfTestCases):
        n, m = map(int, data.readline().split())
        citizens = []
        biggest = 0
        for c in range(0, n):
            citizens.append(Citizen())
        for i in range(0, m):
            a, b = map(int, data.readline().split())
            size = FindFriends(citizens[a-1], citizens[b-1])
            if(size > biggest):
                biggest = size
        result += str(biggest) + '\n'
    print(result)
    return
start = time.clock()
main()
end = time.clock()
print(end-start)

