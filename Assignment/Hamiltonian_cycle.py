class HamiltonianCycle:
    """
    Finds a Hamiltonian Cycle in an undirected graph using backtracking.
    The graph is represented as an adjacency matrix.
    """

    def __init__(self, graph):
        self.graph = graph
        self.n = len(graph)
        self.path = []

    def is_safe(self, vertex, pos):
        """Check whether it is safe to place vertex at the given position in the path."""
        # Check if there is an edge from the previously added vertex to this one
        if self.graph[self.path[pos - 1]][vertex] == 0:
            return False

        # Check if vertex has already been included in the path
        if vertex in self.path:
            return False

        return True

    def solve(self, pos):
        """Use backtracking to build the Hamiltonian path."""
        # Base case: all vertices are included
        if pos == self.n:
            # Check if there is an edge from the last vertex back to the first
            if self.graph[self.path[pos - 1]][self.path[0]] == 1:
                return True
            return False

        # Try each vertex as the next candidate (skip vertex 0 — it's the start)
        for vertex in range(1, self.n):
            if self.is_safe(vertex, pos):
                self.path.append(vertex)

                if self.solve(pos + 1):
                    return True

                # Backtrack
                self.path.pop()

        return False

    def find_cycle(self):
        """
        Entry point to find a Hamiltonian Cycle.
        Returns the cycle as a list if found, otherwise returns None.
        """
        self.path = [0]  # Always start from vertex 0

        if not self.solve(1):
            return None

        # Append the starting vertex to close the cycle
        self.path.append(self.path[0])
        return self.path


def main():
    # Example 1: Graph that contains a Hamiltonian Cycle
    graph1 = [
        [0, 1, 0, 1, 0],
        [1, 0, 1, 1, 1],
        [0, 1, 0, 0, 1],
        [1, 1, 0, 0, 1],
        [0, 1, 1, 1, 0],
    ]

    # Example 2: Graph that does NOT contain a Hamiltonian Cycle
    graph2 = [
        [0, 1, 0, 0],
        [1, 0, 1, 1],
        [0, 1, 0, 0],
        [0, 1, 0, 0],
    ]

    for i, graph in enumerate([graph1, graph2], start=1):
        print(f"Graph {i}")
        print("-" * 30)
        hc = HamiltonianCycle(graph)
        result = hc.find_cycle()

        if result:
            cycle_str = " -> ".join(str(v) for v in result)
            print(f"Hamiltonian Cycle found: {cycle_str}")
        else:
            print("No Hamiltonian Cycle exists in this graph.")
        print()


if __name__ == "__main__":
    main()
