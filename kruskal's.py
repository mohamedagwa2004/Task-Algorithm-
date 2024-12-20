# Union-Find (Disjoint Set) data structure implementation
class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))  # Initially, each node is its own parent
        self.rank = [0] * n  # Rank is used to optimize the union operation

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])  # Path compression
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u != root_v:
            # Union by rank
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1
            return True
        return False

# Kruskal's Algorithm to find the Minimum Spanning Tree (MST)
def kruskal(n, edges):
    # Sort edges by weight
    edges.sort(key=lambda x: x[2])  # (u, v, weight)

    # Create a Disjoint Set to keep track of connected components
    dsu = DisjointSet(n)
    mst = []
    mst_weight = 0

    for u, v, weight in edges:
        if dsu.union(u, v):
            mst.append((u, v, weight))
            mst_weight += weight
            # If we've already selected n-1 edges, we can stop early
            if len(mst) == n - 1:
                break
    
    return mst, mst_weight

# Example Usage
n = 4  # Number of vertices
edges = [
    (0, 1, 10),
    (0, 2, 6),
    (0, 3, 5),
    (1, 3, 15),
    (2, 3, 4)
]

mst, mst_weight = kruskal(n, edges)
print("Edges in MST:", mst)
print("Total weight of MST:", mst_weight)
Explanation of the Code:
DisjointSet class: This class manages the connected components using path compression and union by rank for efficient operations.
kruskal function: The main function implementing Kruskal's algorithm. It:
Sorts the edges by weight.
Uses the union method to add edges to the MST, ensuring that no cycles are formed.
Stops when the MST contains 
𝑉
−
1
V−1 edges.
Output Example:
yaml
Copy code
Edges in MST: [(2, 3, 4), (0, 3, 5), (0, 1, 10)]
Total weight of MST: 19
Key Concepts and Considerations:
Time Complexity:
Sorting the edges: 
𝑂
(
𝐸
log
⁡
𝐸
)
O(ElogE), where 
𝐸
E is the number of edges.
Union-Find operations (with path compression and union by rank) take almost constant time, 
𝑂
(
𝛼
(
𝑉
)
)
O(α(V)), where 
𝛼
α is the inverse Ackermann function.
Space Complexity: The space complexity is 
𝑂
(
𝑉
+
𝐸
)
O(V+E), where 
𝑉
V is the number of vertices and 
𝐸
E is the number of edges.
By implementing Kruskal's algorithm, you can efficiently find the MST for a network and ensure optimal connectivity with the minimum cost.


You said:
implemention kruskal's algorithms
ChatGPT said:
ChatGPT
Sure! Here is a complete Python implementation of Kruskal's Algorithm to find the Minimum Spanning Tree (MST) of a graph. The algorithm uses a Disjoint Set (Union-Find) data structure to efficiently manage the sets of connected components.

Steps:
Sort edges by weight.
Iterate through sorted edges and add edges to the MST if they connect two distinct components (using union-find).
Return the MST once all vertices are connected or 
𝑉
−
1
V−1 edges are selected.
Python Code:
python
Copy code
# Disjoint Set (Union-Find) data structure with path compression and union by rank
class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))  # Each node is its own parent initially
        self.rank = [0] * n  # Rank (used to keep the tree flat)

    def find(self, u):
        if self.parent[u] != u:
            # Path compression: Flatten the structure to make future finds faster
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        # Union by rank: attach the smaller tree under the larger one
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1
            return True
        return False

# Kruskal's Algorithm to find the MST
def kruskal(n, edges):
    # Sort edges based on weight
    edges.sort(key=lambda x: x[2])  # Each edge is a tuple (u, v, weight)

    # Initialize Disjoint Set (Union-Find)
    dsu = DisjointSet(n)
    mst = []  # List to store edges of the MST
    mst_weight = 0  # To store the total weight of the MST

    # Process edges in sorted order
    for u, v, weight in edges:
        if dsu.union(u, v):
            mst.append((u, v, weight))  # Add the edge to the MST
            mst_weight += weight  # Update the total weight of the MST

            # If we've added n-1 edges, the MST is complete
            if len(mst) == n - 1:
                break

    return mst, mst_weight

# Example Usage
if __name__ == "__main__":
    n = 4  # Number of vertices (nodes)
    edges = [
        (0, 1, 10),  # Edge between node 0 and 1 with weight 10
        (0, 2, 6),   # Edge between node 0 and 2 with weight 6
        (0, 3, 5),   # Edge between node 0 and 3 with weight 5
        (1, 3, 15),  # Edge between node 1 and 3 with weight 15
        (2, 3, 4)    # Edge between node 2 and 3 with weight 4
    ]

    mst, mst_weight = kruskal(n, edges)
    print("Edges in MST:", mst)
    print("Total weight of MST:", mst_weight)