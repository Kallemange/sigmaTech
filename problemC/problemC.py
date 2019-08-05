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
https://github.com/mpfeifer1/Kattis/blob/master/shibuyacrossing.cpp

'''

#path="C:/Users/kalle/Documents/Sigma/sigmaTech/problemC"
#ex1=path+"/1.in"
#ex2=path+"/2.in"
#ex3=path+"/3.in"

# Finds all maximal cliques in a graph using the Bron-Kerbosch algorithm. The input graph here is
# in the adjacency list format, a dict with vertexes as keys and lists of their neighbors as values.
# https://en.wikipedia.org/wiki/Bron-Kerbosch_algorithm
import sys
from collections import defaultdict

def find_cliques(graph):
  p = set(graph.keys())
  r = set()
  x = set()
  cliques = []
  for v in degeneracy_ordering(graph):
    neighs = graph[v]
    find_cliques_pivot(graph, r.union([v]), p.intersection(neighs), x.intersection(neighs), cliques)
    p.remove(v)
    x.add(v)
  #return sorted(cliques, lambda x: len(x))
  return sorted(cliques)

def find_cliques_pivot(graph, r, p, x, cliques):
  if len(p) == 0 and len(x) == 0:
    cliques.append(r)
  else:

    #u = iter(p.union(x)).next()
    #Testing another version of iterating
    u = next(iter(p.union(x)))
    for v in p.difference(graph[u]):
      neighs = graph[v]
      find_cliques_pivot(graph, r.union([v]), p.intersection(neighs), x.intersection(neighs), cliques)
      p.remove(v)
      x.add(v)

def degeneracy_ordering(graph):
  ordering = []
  ordering_set = set()
  degrees = defaultdict(lambda : 0)
  degen = defaultdict(list)
  max_deg = -1
  for v in graph:
    deg = len(graph[v])
    degen[deg].append(v)
    degrees[v] = deg
    if deg > max_deg:
      max_deg = deg

  while True:
    i = 0
    while i <= max_deg:
      if len(degen[i]) != 0:
        break
      i += 1
    else:
      break
    v = degen[i].pop()
    ordering.append(v)
    ordering_set.add(v)
    for w in graph[v]:
      if w not in ordering_set:
        deg = degrees[w]
        degen[deg].remove(w)
        if deg > 0:
          degrees[w] -= 1
          degen[deg - 1].append(w)

  ordering.reverse()
  return ordering



def main(path=0):

    n=[]
    m=[]
    if path==0:
        for line in sys.stdin:
            line=line.split()
            n.append(int(line[0]))
            m.append(int(line[1]))
    '''
    else:
        file=open(path, 'r')
        for line in file:
            line=line.split()
            n.append(int(line[0]))
            m.append(int(line[1]))
        file.close()
    '''
    #number of
    #print("n:",n)
    #print("m",m)
    N=n.pop(0)
    M=m.pop(0)
    testDict={}
    #print("N:",N)
    #print("M:",M)
    #print("n:",n)
    #print("m:",m)
    for i in range(M):
        #print("i:", i)
        #print("n[i]", n[i])
        if n[i] in testDict:
            testDict[n[i]].append(m[i])
        else:
            testDict[n[i]]=[m[i]]
        if m[i] in testDict:
            testDict[m[i]].append(n[i])
        else:
            testDict[m[i]]=[n[i]]
    #print(testDict)

    cliques=find_cliques(testDict)
    maxClique=1
    for i in cliques:
        if len(i)>maxClique:
            maxClique=len(i)
    print(maxClique)
    #print(cliques)

if __name__ == '__main__':
    #main(ex1)
    #main(ex2)
    #main(ex3)
    main()
