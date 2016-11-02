import sys

def main():
    #data = sys.stdin
    data = open(r"tests\10878.txt", 'r')
    mylist = data.read().splitlines()
    result = ""
    for line in mylist[1:-1]:
        bitstring = ""
        for char in line:
            if(char == 'o'):
                bitstring += "1"
            elif(char == ' '):
                bitstring += "0"
        result += chr(int(bitstring, 2))
    print(result, end = "")
    return
main()
