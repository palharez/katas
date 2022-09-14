class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        def parse_to_adjency_lis(edges):
            graph = {}

            for f, t in edges:
                if graph.get(f):
                    graph[f].append(t)
                else:
                    graph[f] = [t]

                if not graph.get(t):
                    graph[t] = []

            return graph

        def dfs(src, graph, visited, non_vertice):
            if visited.get(src):
                non_vertice[src] = True
                return

            visited[src] = True

            for neighbor in graph[src]:
                dfs(neighbor, graph, visited, non_vertice)

        visited = {}
        non_vertice = {}
        graph = parse_to_adjency_lis(edges)

        for node in graph.keys():
            dfs(node, graph, visited, non_vertice)

        non_vertice_nodes = non_vertice.keys()

        vertices = list(filter(lambda n: n not in non_vertice_nodes, visited.keys()))

        return vertices
