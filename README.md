# sigmaTech
Repo for solving the assignments given by Sigma Technology.


## Problem C:
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

### Another representation of sample input 2
Here, it's shown as a graph with vertices as row-column names, x as adjacent and 0 as not adjacent.

|v |1|2|3|4|5|
|-|-|-|-|-|-|
|1|-|0|x|x|x|
|2|0|-|x|x|x|
|3|x|x|-|x|0|
|4|x|x|x|-|0|
|5|x|x|0|0|-|

### Permutation Diagram Solution
Another method looks at the permutation diagram, where the vertices are remapped in greatest order
of those that is adjacent to the lowest order. From here a longest decreasing subsequence can be 
produced, which will correspond to the largest clique size. It is briefly introduced here:
https://en.wikipedia.org/wiki/Permutation_graph
as well as:
http://old.kumlander.eu/Clique.htm

Ex. of solved algorithm:
This implementation closely resembles the solution here:
https://github.com/lukaszantkowiak/kattis/blob/master/src/main/java/ShibuyaCrossing.java

<<<<<<< HEAD
Using this method, sample input 2 is remapped as shown in figure below, for which the longest
decreasing subsequence can be counted quickly
=======

>>>>>>> b94dc8f11aea8af63192f307dc1b7265e4993780
![alt text](https://github.com/Kallemange/sigmaTech/blob/master/problemC/permutation.jpg)
