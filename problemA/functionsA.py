#Functions file for problem A provided by Sigma Technology
import sys



def appendCity(name, Citylist):
    if name in Citylist:
        return
    else:
        Citylist.append(name)


if __name__ == "__main__":
    readFile(0)
