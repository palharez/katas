class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        graph = self.build_graph(graph)

        target = len(graph) - 1

        queue = [[0, [0]]]

        paths = []

        while queue:
            node, path = queue.pop(0)

            if node == target:
                paths.append(path)
                continue

            for neighbor in graph[node]:
                neighbor_path = path.copy() + [neighbor]
                queue.append([neighbor, neighbor_path])

        return paths

    def build_graph(self, edges):
        graph = {}

        for node, neighbors in enumerate(edges):
            graph[node] = neighbors

        return graph
