import sys
import time
'''
3 1 = 1
3

3 2 = 4
0 3 # 3 1
1 2 # 2 1
2 1 # 1 1
3 0 # 0 1

3 3 = 10
0 0 3 # 3 2
0 1 2
0 2 1
0 3 0

1 0 2 # 2 2
1 1 1
1 2 0

2 0 1 # 1 2
2 1 0

3 0 0 # 0 2

3 4 = 20
0 0 0 3 #3 3 = 10
0 0 1 2
0 0 2 1
0 0 3 0
0 1 0 2
0 1 1 1
0 1 2 0
0 2 0 1
0 2 1 0
0 3 0 0

1 0 0 2 #2 3 = 6
1 0 1 1
1 0 2 0
1 1 0 1
1 1 1 0
1 2 0 0


2 0 0 1 #1 3 = 3
2 0 1 0
2 1 0 0

3 0 0 0 #0 3 = 1
'''
memo = {}

def howAdd(n, k):
    if((n,k) in memo):
        return memo[(n,k)]
    if(k == 1):
        return 1
    elif(k == 0):
        return 0
    elif(n == 0):
        return 1
    result = 0
    for i in range(0, n+1):
        result += howAdd(i, k-1)
    memo[(n, k)] = result
    #print(n, k, result)
    return result

def main():
    #data = sys.stdin
    data = open(r"tests\10943.txt", 'r')
    n, k = map(int, data.readline().split())
    result = ""
    while(n != 0 and k != 0):
        result += str(howAdd(n, k)%1000000) + '\n'
        n, k = map(int, data.readline().split())
    print(result, end = '')
    return
start = time.time()
main()
end = time.time()
print(end-start)
