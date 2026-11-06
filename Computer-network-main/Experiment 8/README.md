# Experiment 8 - Distance Vector and Link State Routing Algorithms

Aim:

To calculate routes using a Bellman-Ford-based distance-vector simulation and Dijkstra link-state routing.

Algorithm:

1. Represent A-B=1, A-C=4, B-C=2, B-D=6 and C-D=3 in an undirected cost matrix.
2. Initialize each router's distance vector with its own direct link costs.
3. Exchange previous-round neighbor vectors and relax routes until no cost changes.
4. Display all distance-vector costs and next hops.
5. For each source, run Dijkstra using the complete link-state cost matrix.
6. Reconstruct and display shortest paths and total costs.

Program / Commands:

[Source: main.py](main.py)

```powershell
python main.py
```
All sample link costs are positive. Infinity represents a missing link. Distance-vector updates use neighbor information from the preceding round; link-state calculations use the complete topology. The program simulates route calculation, not live routing packets.

Output / Observation:

Execution Status: Verified

All source-destination costs were checked independently with Floyd-Warshall, and displayed link-state path costs were checked against the topology. An unreachable-node case was also verified.

```text
Distance Vector: source destination next-hop cost
A A A 0
A B B 1
A C B 3
A D B 6
B A A 1
B B B 0
B C C 2
B D C 5
C A B 3
C B B 2
C C C 0
C D D 3
D A C 6
D B C 5
D C C 3
D D D 0
Link State: source destination path cost
A A A 0
A B A->B 1
A C A->B->C 3
A D A->B->C->D 6
B A B->A 1
B B B 0
B C B->C 2
B D B->C->D 5
C A C->B->A 3
C B C->B 2
C C C 0
C D C->D 3
D A D->C->B->A 6
D B D->C->B 5
D C D->C 3
D D D 0
```
