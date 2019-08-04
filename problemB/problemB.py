#Problem B for Sigma Technology
'''
Solve a max # tests performed to get an I_max value
Test will be performed by finding max amount of test needed.
The method is iteratively updated,
BRUTE FORCE Solution
1)
Investigating the first 12 situations, we get a solution looking like:
I_max:  1| 2| 3| 4| 5| 6| 7| 8| 9| 10| 11| 12|
x:      0| 1| 2| 2| 3| 3| 3| 4| 4| 4 |  4|  5|
Indicating that the solution is a series where the number corresponds to an
inductive sum such that the I_max <=1+2+...+m for some m. e.g. 1+2+3<8<1+2+3+4=10
thus I_max=8-->4 tests

'''

import math
import sys
import fileinput
path="C:/Users/kalle/Documents/Sigma/sigmaTech/problemB/batteries.in"

def calcMinForI():
    I_max=4711
    x=[0, 0]
    i=0
    while len(x)<I_max:
        x+=[i]*i
        i+=1
    return x

def main(path=0):
    values=[]
    #Read from log file
    if path !=0:
        file=open(path, 'r')
        for line in file:
            if int(line)!=0:
                values.append(int(line.rstrip('\n')))
            else:
                break
        file.close()
    #Read from terminal (for kattis)
    else:
        for line in sys.stdin:
            if int(line)!=0:
                values.append(int(line.rstrip('\n')))
            else:
                break
    series=calcMinForI()
    for i in values:
        print(series[i])

if __name__ == "__main__":
    main(0)
    #main(path)
