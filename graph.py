import random
import numpy as np

class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.adj_matrix = np.zeros((vertices, vertices))
        self.adj_list = [[] for _ in range(vertices)]
    
    def add_edge(self, u, v, weight=1):
        if u >= self.V or v >= self.V or u < 0 or v < 0:
            raise ValueError("Невірний індекс вершини")
        if u == v:
            raise ValueError("Петлі заборонені в графі (ребро до тієї ж вершини)")
        if self.adj_matrix[u][v] != 0:
            raise ValueError("Ребро вже існує")
            
        self.adj_matrix[u][v] = weight
        self.adj_matrix[v][u] = weight
        if not v in self.adj_list[u]:
            self.adj_list[u].append(v)
        if not u in self.adj_list[v]:
            self.adj_list[v].append(u)
    
    def matrix_to_list(self):
        self.adj_list = [[] for _ in range(self.V)]
        for i in range(self.V):
            for j in range(self.V):
                if self.adj_matrix[i][j] != 0:
                    self.adj_list[i].append(j)
    
    def list_to_matrix(self):
        self.adj_matrix = np.zeros((self.V, self.V))
        for i in range(self.V):
            for j in self.adj_list[i]:
                self.adj_matrix[i][j] = 1
                self.adj_matrix[j][i] = 1
    
    @staticmethod
    def generate_random(vertices, density):
        graph = Graph(vertices)

        for i in range(vertices):
            for j in range(i + 1, vertices):
                if random.random() < density:
                    graph.add_edge(i, j)
        
        return graph
    
    @property
    def density(self):
        max_edges = (self.V * (self.V - 1)) // 2
        actual_edges = sum(sum(row) for row in self.adj_matrix) // 2
        return actual_edges / max_edges if max_edges > 0 else 0
    
    def get_degree(self, vertex):
        return len(self.adj_list[vertex])
    
    def get_all_degrees(self):
        return {i: self.get_degree(i) for i in range(self.V)}
    
    def get_max_degree(self):
        return max(self.get_degree(v) for v in range(self.V))
    
    def get_min_degree(self):
        return min(self.get_degree(v) for v in range(self.V))
    
    def add_vertex(self):
        self.V += 1
        new_matrix = np.zeros((self.V, self.V))
        new_matrix[:-1, :-1] = self.adj_matrix
        self.adj_matrix = new_matrix
        self.adj_list.append([])

    def remove_vertex(self, v):
        if v < 0 or v >= self.V:
            raise ValueError("Невірний індекс вершини")

        self.adj_matrix = np.delete(np.delete(self.adj_matrix, v, 0), v, 1)

        self.adj_list.pop(v)
        for neighbors in self.adj_list:
            if v in neighbors:
                neighbors.remove(v)
            for i in range(len(neighbors)):
                if neighbors[i] > v:
                    neighbors[i] -= 1
        
        self.V -= 1

    def remove_edge(self, u, v):
        if u >= self.V or v >= self.V:
            raise ValueError("Невірний індекс вершини")
        
        self.adj_matrix[u][v] = 0
        self.adj_matrix[v][u] = 0
        
        if v in self.adj_list[u]:
            self.adj_list[u].remove(v)
        if u in self.adj_list[v]:
            self.adj_list[v].remove(u)

    def dfs(self, v, visited):
        visited[v] = True
        for neighbor in self.adj_list[v]:
            if not visited[neighbor]:
                self.dfs(neighbor, visited)

    def is_connected(self):
        vertices_with_edges = set()
        for i in range(self.V):
            if self.adj_list[i]:
                vertices_with_edges.add(i)
            for j in range(self.V):
                if self.adj_matrix[i][j] != 0:
                    vertices_with_edges.add(j)
        
        if not vertices_with_edges:
            return True

        start_vertex = min(vertices_with_edges)
        visited = [False] * self.V
        self.dfs(start_vertex, visited)

        return all(visited[v] for v in vertices_with_edges)

    def is_planar(self):
        if self.V <= 4:
            return True

        edges_count = sum(sum(row) for row in self.adj_matrix) // 2
        if edges_count > 3 * self.V - 6:
            return False

        if self.V >= 5:
            k5_found = True
            for i in range(5):
                for j in range(i + 1, 5):
                    if self.adj_matrix[i][j] == 0:
                        k5_found = False
                        break
                if not k5_found:
                    break
            if k5_found:
                return False

        if self.V >= 6:
            vertices = list(range(self.V))
            from itertools import combinations
            for part1 in combinations(vertices, 3):
                part2 = [v for v in vertices if v not in part1]
                if len(part2) >= 3:
                    for part2_subset in combinations(part2, 3):
                        k33_found = True
                        for v1 in part1:
                            for v2 in part2_subset:
                                if self.adj_matrix[v1][v2] == 0:
                                    k33_found = False
                                    break
                            if not k33_found:
                                break
                        if k33_found:
                            return False
        
        return True
