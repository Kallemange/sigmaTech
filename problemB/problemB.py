#Problem B for Sigma Technology
'''
Solve a max # tests performed to get an I_max value
Test will be performed by finding max amount of test needed.
The method is iteratively updated, in versions
    1) for a given constant step size, iterate through the k<n/2 and calculate x_max
    as x=floor(n/k)+k
    2) TBA

IN sys.stdin/textfile
int[]: read input until 0, terminate reading
OUT sys.stdout/print
int[]: minimal max number of tests for any series of max ampere value
'''

import sys
import fileinput
path="C:/Users/kalle/Documents/Sigma/sigmaTech/problemB/batteries.in"

def calcMinTest(n):
    return 0

def main(path=0):
    text=[]
    if path !=0:
        file=open(path, 'r')
        for line in file:
            if int(line)!=0:
                text.append(int(line.rstrip('\n')))
            else:
                break
        file.close()
    else:
        for line in sys.stdin:
            if int(line)!=0:
                text.append(int(line.rstrip('\n')))
            else:
                break
    #print(text)
    #text=text.split()
    print(calcMinTest(1))


if __name__ == "__main__":
    #main(0)
    main(path)
