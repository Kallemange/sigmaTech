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

import sys
import time
#import maximal_cliques as mc
t0=time.time()
#import networkx as nx
def find_cliques(G):
    if len(G) == 0:
        return

    adj = {u: {v for v in G[u] if v != u} for u in G}
    Q = [None]

    subg = set(G)
    cand = set(G)
    u = max(subg, key=lambda u: len(cand & adj[u]))
    ext_u = cand - adj[u]
    stack = []

    try:
        while True:
            if ext_u:
                q = ext_u.pop()
                cand.remove(q)
                Q[-1] = q
                adj_q = adj[q]
                subg_q = subg & adj_q
                if not subg_q:
                    yield Q[:]
                else:
                    cand_q = cand & adj_q
                    if cand_q:
                        stack.append((subg, cand, ext_u))
                        Q.append(None)
                        subg = subg_q
                        cand = cand_q
                        u = max(subg, key=lambda u: len(cand & adj[u]))
                        ext_u = cand - adj[u]
            else:
                Q.pop()
                subg, cand, ext_u = stack.pop()
    except IndexError:
        pass

class Graph(object):
    node_dict_factory = dict
    node_attr_dict_factory = dict
    adjlist_outer_dict_factory = dict
    adjlist_inner_dict_factory = dict
    edge_attr_dict_factory = dict
    graph_attr_dict_factory = dict
    def __len__(self):
        return len(self._node)

    def __init__(self, incoming_graph_data=None, **attr):
        self.graph_attr_dict_factory = self.graph_attr_dict_factory
        self.node_dict_factory = self.node_dict_factory
        self.node_attr_dict_factory = self.node_attr_dict_factory
        self.adjlist_outer_dict_factory = self.adjlist_outer_dict_factory
        self.adjlist_inner_dict_factory = self.adjlist_inner_dict_factory
        self.edge_attr_dict_factory = self.edge_attr_dict_factory

        self.graph = self.graph_attr_dict_factory()   # dictionary for graph attributes
        self._node = self.node_dict_factory()  # empty node attribute dict
        self._adj = self.adjlist_outer_dict_factory()  # empty adjacency dict
        # attempt to load graph with data
        if incoming_graph_data is not None:
            convert.to_networkx_graph(incoming_graph_data, create_using=self)
        # load graph attributes (must be after convert)
        self.graph.update(attr)
    def add_edge(self, u_of_edge, v_of_edge, **attr):
        u, v = u_of_edge, v_of_edge
        # add nodes
        if u not in self._node:
            self._adj[u] = self.adjlist_inner_dict_factory()
            self._node[u] = self.node_attr_dict_factory()
        if v not in self._node:
            self._adj[v] = self.adjlist_inner_dict_factory()
            self._node[v] = self.node_attr_dict_factory()
        # add the edge
        datadict = self._adj[u].get(v, self.edge_attr_dict_factory())
        datadict.update(attr)
        self._adj[u][v] = datadict
        self._adj[v][u] = datadict

#from networkx import Graph
#print("time0:", time.time()-t0)
def main(path=0):

    n=[]
    m=[]
    t0=None
    G=Graph()
    if path==0:
        for line in sys.stdin:
            line=line.split()
            n.append(int(line[0]))
            m.append(int(line[1]))

        M=m.pop(0)
        for i in range(M):
            G.add_edge(int(n[i]), int(m[i]))

    else:
        t0=time.time()
        file=open(path, 'r')
        mn=file.readline().split()
        N=int(mn[0])
        M=int(mn[1])
        for line in file:
            line=line.split()
            G.add_edge(int(line[0]), int(line[1]))
            #n.append(int(line[0]))
            #m.append(int(line[1]))
        file.close()
    test=list(find_cliques(G))
    maxGraph=1
    for i in test:
        if len(i)>maxGraph:
            maxGraph=len(i)
    print(maxGraph)

    #print(graphDict)
    #if t0 is not None:
        #print("Time2: ",time.time()-t0
    #print(cliques)
    #if t0 is not None:
        #print("Time3: ",time.time()-t0)


    #print(cliques)

if __name__ == '__main__':
    path="C:/Users/kalle/Documents/Sigma/sigmaTech/problemC"
    ex1=path+"/1.in"
    ex2=path+"/2.in"
    ex3=path+"/3.in"
    ex5=path+"/5.in"
    ex6=path+"/6.in"
    #main(ex1)
    #main(ex2)
    #main(ex6)
    main(ex2)
