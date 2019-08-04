#problem C for Sigma Technology
#Karl Lundin
path="C:/Users/kalle/Documents/Sigma/sigmaTech/problemC"
ex1=path+"/1.in"
ex2=path+"/2.in"

'''
The problem can be considered finding the largest fully connected clique in a graph.
People represent a vertex, bumping together is being adjacent. It can then be
presented as a numbered graph, with all adjacent vertices given for a vertex.
this is presented in
https://en.m.wikipedia.org/wiki/Clique_(graph_theory)
and can be solved using a greedy algorithm given as:
Starting with an arbitrary clique (for instance, any single vertex or even the
empty set), grow the current clique one vertex at a time by looping through the
graph's remaining vertices. For each vertex v that this loop examines, add v to
the clique if it is adjacent to every vertex that is already in the clique, and
discard v otherwise.
"https://en.wikipedia.org/wiki/Clique_problem#Finding_a_single_maximal_clique"

Also presented by Östergård:
"A fast algorithm for the maximum clique problem"

Another representation of sample input 2
_|1|2|3|4|5
1|-|0|x|x|x
2|0|-|x|x|x
3|x|x|-|x|0
4|x|x|x|-|0
5|x|x|0|0|-

Ex. of solved algorithm:
https://github.com/mpfeifer1/Kattis/blob/master/shibuyacrossing.cpp

'''


def main(path):
    file=open(path, 'r')
    n=[]
    m=[]
    for line in file:
        line.split()
        n.append(int(line[0]))
        m.append(int(line[2]))
    file.close()
    #print(n)
    #print(m)

if __name__ == '__main__':
    main(ex1)
    #main(ex2)
