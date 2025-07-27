class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        indices = []
        for i, string in enumerate(words):
            if x in string:
                indices.append(i)
        return indices
