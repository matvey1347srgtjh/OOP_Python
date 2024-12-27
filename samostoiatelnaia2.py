class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_edge(self, u, v):
        
        if u not in self.adjacency_list:
            self.adjacency_list[u] = []
        if v not in self.adjacency_list:
            self.adjacency_list[v] = []
        self.adjacency_list[u].append(v)
        self.adjacency_list[v].append(u) 

    def display(self):
        
        for vertex, edges in self.adjacency_list.items():
            print(f"{vertex}: {', '.join(map(str, edges))}")

    def dfs(self, start):
       
        visited = set()
        self._dfs_recursive(start, visited)

    def _dfs_recursive(self, vertex, visited):
        
        visited.add(vertex)
        print(vertex, end=' ')
        for neighbor in self.adjacency_list.get(vertex, []):
            if neighbor not in visited:
                self._dfs_recursive(neighbor, visited)

    def bfs(self, start):
        
        visited = set()
        queue = [start]
        visited.add(start)

        while queue:
            vertex = queue.pop(0)
            print(vertex, end=' ')
            for neighbor in self.adjacency_list.get(vertex, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)


if __name__ == "__main__":
    g = Graph()
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 4)
    g.add_edge(2, 5)
    g.add_edge(3, 6)

    print("Граф:")
    g.display()

    print("\nПоиск в глубину (начиная с 1):")
    g.dfs(1)

    print("\n\nПоиск в ширину (начиная с 1):")
    g.bfs(1)
