# link
# https://www.hackerrank.com/challenges/simple-array-sum/problem

#!/bin/python3
def simpleArraySum(ar):
    return sum(ar)

if __name__ == '__main__':

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)

    print(result)
