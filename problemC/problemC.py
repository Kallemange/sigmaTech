#problem C for Sigma Technology
#Karl Lundin
'''
The problem can be considered finding the largest fully connected clique in a graph.
People represent a vertex, bumping together is an edge and any two vertices connected
by an edge are called adjacent. It can then be considered an undirected graph,
with all edges given for a vertex. This is presented in
https://en.m.wikipedia.org/wiki/Clique_(graph_theory)
and can be solved using a greedy algorithm given as:
Starting with an arbitrary clique (for instance, any single vertex or even the
empty set), grow the current clique one vertex at a time by looping through the
graph's remaining vertices. For each vertex v that this loop examines, add v to
the clique if it is adjacent to every vertex that is already in the clique, and
discard v otherwise.
"https://en.wikipedia.org/wiki/Clique_problem#Finding_a_single_maximal_clique"

Another representation of sample input 2
_|1|2|3|4|5
1|-|0|x|x|x
2|0|-|x|x|x
3|x|x|-|x|0
4|x|x|x|-|0
5|x|x|0|0|-

Also presented by Östergård:
"A fast algorithm for the maximum clique problem"
shows an algorith for solving this problem:
function clique(U,size)
    if |U|=0 then
        if size>max then
            max:=size
            New record; save it.
        end if
        return:
    end if
    while U=/= {empty} do
        if size + |U| <= max then
            return
        end if
        i:=min{j|v_j in U}
        U:=U\{v_i}
        clique(U and N(v_i), size+1)
    end while
    return
function old
    max:=0
    clique(V,0)
    return

Ex. of solved algorithm:
This implementation copies that of this method:
https://github.com/lukaszantkowiak/kattis/blob/master/src/main/java/ShibuyaCrossing.java

'''

import sys
#import maximal_cliques as mc
def permutationDiagram(graph, N):
    perm=[]
    for i in range(N):
        before=[]
        for j in range(i):
            if i in graph[j]:
                before.append(j)
        if before==[]:
            perm.append(i)
        else:
            min = 100000
            for b in before:
                p = perm.index(b)
                if (p<min):
                    min = p
            perm.insert(min, i)
    return perm

def longestSeq(seq):
    lengths=[0]*len(seq)
    lengths[0]=1
    max=1
    for i in range(1,len(seq)):
        maxt=0
        for j in range(len(seq)):
            if seq[j]>seq[i] and lengths[j]>maxt:
                maxt =lengths[j]
        lengths[i]=maxt+1
        if lengths[i]>max:
            max=lengths[i]
    return max

def main(path=0):
    n=[]
    m=[]
    t0=None
    graphDict={}
    if path==0:
        line=sys.stdin.readline()
        line=line.split()
        M=int(line[1])
        N=int(line[0])
        for line in sys.stdin:
            line=line.split()
            n.append(int(line[0])-1)
            m.append(int(line[1])-1)

    else:
        file=open(path, 'r')
        mn=file.readline().split()
        N=int(mn[0])
        M=int(mn[1])
        for line in file:
            line=line.split()
            n.append(int(line[0])-1)
            m.append(int(line[1])-1)
        file.close()
    graph={}
    for i in range(N):
        graph[i]=[]
    for i in range(M):
        graph[n[i]].append(m[i])
    perm=permutationDiagram(graph, N)
    #print(perm)
    print(longestSeq(perm))

main()
if __name__ == '__main__':
    path="C:/Users/kalle/Documents/Sigma/sigmaTech/problemC"
    ex1=path+"/1.in"
    ex2=path+"/2.in"
    ex3=path+"/3.in"
    ex5=path+"/5.in"
    ex6=path+"/6.in"
    ex7=path+"/7.in"
    #main(ex1)
    #main(ex2)
    main(ex3)
    #main()
