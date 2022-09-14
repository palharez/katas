class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def parse_to_adjency_list(arr):
            graph = {}

            for i in range(len(arr)):
                graph[i] = []

                for j in range(len(arr[i])):
                    if arr[i][j] and i != j:
                        graph[i].append(j)

            return graph

        def dfs(src, graph, visited):
            if visited.get(src):
                return 0

            visited[src] = True

            for neighbor in graph[src]:
                dfs(neighbor, graph, visited)

            return 1


        graph = parse_to_adjency_list(isConnected)

        visited = {}

        provinces = 0

        for k, v in graph.items():
            provinces += dfs(k, graph, visited)

        return provinces
