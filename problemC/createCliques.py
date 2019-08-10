import random
f= open("6.in","w+")
counter=0
list1 =[]
list2 =[]
n=200
for i in range(1,n):
    for j in range(i+1, 800):
        if counter<10000:
            if random.uniform(0,1)>0.2:
                counter+=1
                list1.append(i)
                list2.append(j)
        else:
            break
f.write(str(n)+ " "+str(len(list1))+"\n")
for i in range(len(list1)):
    f.write(str(list1[i])+" "+ str(list2[i])+"\n")
f.close()
