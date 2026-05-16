from collections import deque


class Graph:
    def __init__(self):
        self.vertices = 5

        self.graph_data = []

        for _ in range(self.vertices):
            row = []

            for _ in range(self.vertices):
                row.append(0)

            self.graph_data.append(row)

    def add_edge(self, u, v):
        self.graph_data[u][v] = 1
        self.graph_data[v][u] = 1

    def display(self):
        print("Adjacency Matrix:")

        for row in self.graph_data:
            print(row)
        print("")
    

    def bfs(self, start):
        visited = []

        for _ in range(self.vertices):
            visited.append(False)

        queue = deque()

        queue.append(start)

        visited[start] = True

        print("BFS Traversal:", end=" ")

        while len(queue) > 0:

            current = queue.popleft()

            print(current, end=" ")

            for neighbor in range(self.vertices):

                if self.graph_data[current][neighbor] == 1:

                    if visited[neighbor] == False:

                        visited[neighbor] = True

                        queue.append(neighbor)

        print("")

    def dfs(self, start):
        visited = []

        for i in range(self.vertices):
            visited.append(False)

        stack = []

        stack.append(start)

        print("DFS Traversal:", end=" ")

        while len(stack) > 0:

            current = stack.pop()

            if visited[current] == True:
                continue

            visited[current] = True

            print(current, end=" ")

            neighbors = []

            for i in range(self.vertices):
                if self.graph_data[current][i] == 1:
                    if visited[i] == False:
                        neighbors.append(i)

            neighbors.reverse()

            for node in neighbors:
                stack.append(node)

        print("")

g = Graph()

g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)

g.display()

g.bfs(0)
print("")
g.dfs(0)
