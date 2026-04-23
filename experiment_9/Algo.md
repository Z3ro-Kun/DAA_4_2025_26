# Greedy Approximation Algorithm for Minimum Subset Sum Difference

## Idea

Divide the array into two subsets by always assigning the next largest element to the subset with the smaller current sum.

---

## Steps

1. Sort the array in **descending order**
2. Initialize two subsets:

   * `set1 = []`, `sum1 = 0`
   * `set2 = []`, `sum2 = 0`
3. Iterate through each element `x` in the sorted array:

   * If `sum1 <= sum2`:

     * Add `x` to `set1`
     * Update `sum1 += x`
   * Else:

     * Add `x` to `set2`
     * Update `sum2 += x`
4. Compute the final difference:

   * `difference = |sum1 - sum2|`

---

## Pseudocode

```
function greedyPartition(arr):
    sort arr in descending order

    set1, set2 = empty lists
    sum1, sum2 = 0, 0

    for x in arr:
        if sum1 <= sum2:
            set1.append(x)
            sum1 += x
        else:
            set2.append(x)
            sum2 += x

    return abs(sum1 - sum2)
```

---

## Complexity

* Time: **O(n log n)** (due to sorting)
* Space: **O(n)**

---

## Note

* This is a **heuristic (approximation)** approach.
* It does **not guarantee the optimal answer** for all inputs.
* Works well in practice but can fail on certain edge cases.
