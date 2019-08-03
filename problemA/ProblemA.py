#Problem A
'''
1) Read a stdin or a .txt
2) Check for first value: # of test cases [int<51]
3) Check for second value: # of trips [int<101]
4) Check for city:
        if(new)
            append
5) Print length (array)

'''
import sys
import fileinput
path="C:/Users/kalle/Documents/Sigma/sigmaTech/problemA/everywhere-01.in"

def main(path=0):
    text=''
    if path !=0:
        file=open(path, 'r')
        for line in file:
            text+=line.rstrip('\n')+' '
    else:
        for line in sys.stdin:
            text+=line.rstrip('\n')+' '
    text=text.split()

    testCases=int((text[0]))
    line=1
    for i in range(testCases):
        if text[line]==' ' or text[line]=='':
            print("empty string")
        cities=text[line]
        line+=1
        citiesVisited=text[line:line+int(cities)]
        line+=int(cities)
        citylist=""
        for city in citiesVisited:
            if city in citylist:
                pass
            else:
                citylist+=city+" "
        print(len(citylist.split()))




if __name__ == "__main__":
    #main(path)
    main()
