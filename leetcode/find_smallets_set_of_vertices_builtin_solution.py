class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        froms = {f for f, _ in edges}
        for _, to in edges:
            froms.discard(to)
        return froms
