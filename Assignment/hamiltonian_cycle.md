# Question 2 — Hamiltonian Cycle

Given an **undirected graph**, determine whether a Hamiltonian cycle exists — a path that visits every vertex exactly once and returns to the starting vertex.

**Tasks:**
- Print one valid cycle if it exists
- Return false otherwise
- Use adjacency matrix representation

---

## Approach

The solution uses **backtracking** on an adjacency matrix. Starting from vertex 0, the algorithm tries to extend the current path one vertex at a time. At each step it checks two conditions before adding a vertex:

1. There must be an edge between the last vertex in the path and the candidate vertex.
2. The candidate vertex must not already be in the path.

When all N vertices have been added, it checks whether an edge exists from the last vertex back to the starting vertex (vertex 0). If yes, a Hamiltonian cycle is complete.

### Adjacency Matrix

A 2D list where `graph[i][j] = 1` means there is an edge between vertex `i` and vertex `j`, and `0` means there is no edge.

```
Example (5-vertex graph):
        0  1  2  3  4
   0  [ 0, 1, 0, 1, 0 ]
   1  [ 1, 0, 1, 1, 1 ]
   2  [ 0, 1, 0, 0, 1 ]
   3  [ 1, 1, 0, 0, 1 ]
   4  [ 0, 1, 1, 1, 0 ]
```

---

## Code

See [`q2_hamiltonian_cycle.py`](q2_hamiltonian_cycle.py)

---

## Results

### Graph 1 — Cycle Exists

Adjacency matrix:

```
     0  1  2  3  4
0  [ 0, 1, 0, 1, 0 ]
1  [ 1, 0, 1, 1, 1 ]
2  [ 0, 1, 0, 0, 1 ]
3  [ 1, 1, 0, 0, 1 ]
4  [ 0, 1, 1, 1, 0 ]
```

**Output:**
```
Graph 1
------------------------------
Hamiltonian Cycle found: 0 -> 1 -> 2 -> 4 -> 3 -> 0
```

The cycle visits every vertex exactly once: **0 → 1 → 2 → 4 → 3 → 0**

---

### Graph 2 — No Cycle Exists

Adjacency matrix:

```
     0  1  2  3
0  [ 0, 1, 0, 0 ]
1  [ 1, 0, 1, 1 ]
2  [ 0, 1, 0, 0 ]
3  [ 0, 1, 0, 0 ]
```

**Output:**
```
Graph 2
------------------------------
No Hamiltonian Cycle exists in this graph.
```

Vertices 2 and 3 both connect only to vertex 1. It is impossible to visit both and return to the start without revisiting vertex 1.

---

## Complexity

| Metric | Value |
|---|---|
| Time Complexity | O(N!) — all permutations explored in the worst case |
| Space Complexity | O(N) for the path array and recursion stack |
| Graph Representation | Adjacency matrix — O(N²) space |

---

## Key Difference from Eulerian Cycle

| Property | Hamiltonian Cycle | Eulerian Cycle |
|---|---|---|
| Visits | Every **vertex** exactly once | Every **edge** exactly once |
| Detection | NP-complete — no efficient algorithm known | Polynomial — check vertex degrees |
