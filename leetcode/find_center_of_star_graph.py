class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        visited = []

        while edges:
            nodes = edges.pop()

            for node in nodes:
                if node in visited:
                    return node
                else:
                    visited.append(node)

        return False
