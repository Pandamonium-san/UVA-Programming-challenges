import sys

class Mobile:
    def __init__(self):
        self.wL = 0
        self.wR = 0
        self.dL = 0
        self.dR = 0
        self.left = None
        self.right = None
    def Weight(self):
        return self.WeightL() + self.WeightR()
    def WeightL(self):
        if(self.wL == 0):
            return self.left.Weight()
        else:
            return self.wL
    def WeightR(self):
        if(self.wR == 0):
            return self.right.Weight()
        else:
            return self.wR
    def IsBalanced(self):
        fL = self.WeightL() * self.dL
        fR = self.WeightR() * self.dR
        if((fL != fR) or
           (self.left and not self.left.IsBalanced()) or
           (self.right and not self.right.IsBalanced())):
            return False
        else:
            return True
            
def CreateMobile(data):
    currLine = data.readline()
    currMobile = Mobile()
    wL, dL, wR, dR = map(int,currLine.split())
    
    currMobile.wL = wL
    currMobile.dL = dL
    currMobile.wR = wR
    currMobile.dR = dR
    
    if(wL == 0):
        currMobile.left = CreateMobile(data)
    if(wR == 0):
        currMobile.right = CreateMobile(data)

    return currMobile

def main():
    #data = sys.stdin
    data = open("tests\839.txt",'r')
    nrOfTestCases = int(data.readline())
    result = ""
    for i in range(0, nrOfTestCases):
        data.readline()
        x = CreateMobile(data)
        if(x.IsBalanced()):
            result += "YES\n"
        else:
            result += "NO\n"
        if(i != nrOfTestCases-1):
            result += "\n"
    print(result,end="")
    return
main()
