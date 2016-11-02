import sys
import time

class Order:
    def __init__(self, amount, id):
        self.id = id
        self.amount = amount
        
def Deliver(a, b):
    amount = abs(a.amount)
    b.amount += a.amount
    a.amount = 0
    #print(amount, "from", p.id, "to", o.id)
    return abs(b.id-a.id) * amount
        
def DoTrading(town):
    buying = []
    selling = []
    for i in range(len(town)):
        if(town[i] >= 0):
            buying.append(Order(town[i], i))
        else:
            selling.append(Order(town[i], i))
    steps = 0
    #print(town)
    for o in buying:
        if(o.amount == 0):
            continue
        for p in selling:
            if(p.amount == 0 or o == p):
                continue
            if(abs(o.amount) >= abs(p.amount)):
                steps += Deliver(p, o)
            else:
                steps += Deliver(o, p)
                break
    return steps

def DoTrading(town):
    balance = 0
    work = 0
    for a in town:
        work += abs(balance)
        balance += a
    return work

def main():
    #data = sys.stdin
    data = open(r"tests\11054.txt", 'r')
    result = ""
    while(True):
        size = int(data.readline())
        if(size == 0):
            break
        town = list(map(int, data.readline().split()))
        result += str(DoTrading(town)) + '\n'
    print(result, end="")
    return

start = time.clock()
main()
end = time.clock()
print('\n', end-start)
