# Question 1 — N-Queens Problem

Place **N queens** on an N×N chessboard such that no two queens attack each other.

**Tasks:**
- Print all possible solutions
- Count the total number of valid configurations
- Optimise using column and diagonal hashing

---

## Approach

The solution uses **backtracking** combined with **hash sets** to efficiently track which columns and diagonals are already occupied.

### Why Hash Sets?

A naive approach checks every placed queen each time we try to place a new one — O(N) per check. Instead, three sets are maintained:

| Set | Tracks | Key |
|---|---|---|
| `cols` | Occupied columns | column index |
| `diag1` | Top-left → bottom-right diagonals | `row - col` (constant along this diagonal) |
| `diag2` | Top-right → bottom-left diagonals | `row + col` (constant along this diagonal) |

This reduces each safety check to **O(1)**.

### Algorithm

1. Start from row 0 and try placing a queen in each column.
2. Before placing, check if the column and both diagonals are free using the sets.
3. If safe, place the queen and add the column/diagonal keys to the sets.
4. Recurse to the next row.
5. If all N rows are filled, record the solution.
6. On backtrack, remove the keys from the sets.

---

## Code

See [`q1_n_queens.py`](q1_n_queens.py)

---

## Results

Running the program for **N = 8**:

### Sample Solutions (first 3 of 92)

**Solution 1:**
```
Q . . . . . . .
. . . . Q . . .
. . . . . . . Q
. . . . . Q . .
. . Q . . . . .
. . . . . . Q .
. Q . . . . . .
. . . Q . . . .
```

**Solution 2:**
```
Q . . . . . . .
. . . . . Q . .
. . . . . . . Q
. . Q . . . . .
. . . . . . Q .
. . . Q . . . .
. Q . . . . . .
. . . . Q . . .
```

**Solution 3:**
```
Q . . . . . . .
. . . . . . Q .
. . . Q . . . .
. . . . . Q . .
. . . . . . . Q
. Q . . . . . .
. . . . Q . . .
. . Q . . . . .
```

> All 92 solutions are printed when the program is run.

### Total Valid Configurations

| N | Total Solutions |
|---|---|
| 1 | 1 |
| 4 | 2 |
| 5 | 10 |
| 6 | 4 |
| 7 | 40 |
| **8** | **92** |

```
========================================
Total valid configurations for 8-Queens: 92
========================================
```

---

## Complexity

| Metric | Value |
|---|---|
| Time Complexity | O(N!) in the worst case |
| Space Complexity | O(N) for the sets and recursion stack |
| Safety Check | O(1) per placement due to hash sets |
