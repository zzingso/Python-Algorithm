# link
# https://www.hackerrank.com/challenges/absolute-permutation/problem


# python HackerRank/Implementation/Medium/AbsolutePermutation.py 

# Sample Input
# 3
# 2 1
# 3 0
# 3 2

# Sample Output
# 2 1
# 1 2 3
# -1

#!/bin/python3

# Complete the absolutePermutation function below.
def absolutePermutation(n, k):
    initArr = [x + 1 for x in range(n)]
    resultArr = []
    
    if len(initArr) % 2 == 0:
        halfLen = len(initArr) // 2
        if k == 0:
            resultArr = initArr
        elif k <= halfLen and halfLen % k == 0:
            for i in range(halfLen // k):
                multiNum = i * k * 2
                resultArr += initArr[multiNum+k:multiNum+(2*k)] 
                resultArr += initArr[multiNum:multiNum+k]
        else:
            resultArr = [-1]
    else:
        resultArr = initArr if k == 0 else [-1]
    
    return resultArr

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        result = absolutePermutation(n, k)

        print(' '.join(map(str, result)))
        print()
