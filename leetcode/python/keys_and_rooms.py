class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        graph = {edge: neighbors for edge, neighbors in enumerate(rooms)}

        visited = {}

        self.dfs(graph, 0, visited)

        return len(visited.keys()) == len(graph.keys())

    def dfs(self, graph, current, visited):
        if visited.get(current): return

        visited[current] = True

        for neighbor in graph[current]:
            self.dfs(graph, neighbor, visited)
