#Problem B for Sigma Technology
'''
Solve a max # tests performed to get an I_max value
Test will be performed by finding max amount of test needed.
The method is iteratively updated, in versions
    1) for a given constant step size, iterate through the k<n/2 and calculate x_max
    as x=floor(n/k)+k
    2) TBA

IN sys.stdin/valuesfile
int[]: read input until 0, terminate reading
OUT sys.stdout/print
int[]: minimal max number of tests for any series of max ampere value
'''
import math
import sys
import fileinput
path="C:/Users/kalle/Documents/Sigma/sigmaTech/problemB/batteries.in"

def calcMinForI(I):
    print("known I: ", I)
    x_best=10000
    if I<2:
        x_best=0
    elif I==2:
        x_best=1
    else:
        X=I
        k=math.ceil(math.sqrt(I))
        counter=0
        print("Iteration ", counter+1, ", k=", k)
        x_1=1+k
        x_2=0
        while k>2:
            X-=k
            k=math.ceil(math.sqrt(X))
            x_2+=1
            counter+=1
            print("Iteration ", counter+1, " k=", k, "interval size: ", X, "max tests=", counter+k)
            if counter>1000:
                break
        #print(x_2)
        x_2+=k
        #print(k)

    '''
        For a value of I_max, and an untested set of values 0<=I<=I_max, there is
        an optimal step size, only related to the size of the interval. Each step
        should be taken at that optimum, meaning the step size will change over
        the iterations. E.g. for a known max value n, the set is X: 0<=I_max<n,
        testing the value k gives either:
            a) k>I_max ==> 0<=I_max<k
            b) k<I_max ==> k<I_max<n
        For a large interval X --> k>>1
        For a small interval X --> k->1

        We should find the value such that (n-1)/k=k <==> k=sqrt(X_max-X_min)
        [still doesn't seem to be an optimal value, I need to investigate more]
    '''
    print(x_best)

def calcMinTest(n):
    for I in n:
        k_min=calcMinForI(I)

def main(path=0):
    values=[]
    if path !=0:
        file=open(path, 'r')
        for line in file:
            if int(line)!=0:
                values.append(int(line.rstrip('\n')))
            else:
                break
        file.close()
    else:
        for line in sys.stdin:
            if int(line)!=0:
                values.append(int(line.rstrip('\n')))
            else:
                break
    calcMinTest(values)


if __name__ == "__main__":
    #main(0)
    main(path)
