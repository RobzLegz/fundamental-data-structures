from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}

    def display(self):
        print("Adjacency List:")
        for node in g.graph:
            print(f"{node} -> {g.graph[node]}")

    def add_edge(self, x, y):
        if x not in self.graph:
            self.graph[x] = []

        if y not in self.graph:
            self.graph[y] = []

        self.graph[x].append(y)

    def bfs(self, start):
        visited = set()
        queue = deque()

        visited.add(start)
        queue.append(start)

        print("BFS Traversal:")

        while queue:
            node = queue.popleft()
            print(node, end=" ")

            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        print("")

    def dfs(self, start):
        visited = set()

        print("DFS Traversal:")
        self._dfs_recursive(start, visited)
        print("")

    def _dfs_recursive(self, node, visited):
        visited.add(node)
        print(node, end=" ")

        for neighbor in self.graph[node]:
            if neighbor not in visited:
                self._dfs_recursive(neighbor, visited)


g = Graph()

g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('B', 'D')
g.add_edge('B', 'E')
g.add_edge('C', 'F')
g.add_edge('E', 'F')

g.display()

print("")

g.bfs('A')
print("")
g.dfs('A')

