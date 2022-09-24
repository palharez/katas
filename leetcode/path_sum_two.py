# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        paths = []
        temp_path = []

        self.dfs(root, targetSum, paths, temp_path)

        return paths

    def dfs(self, root, target, paths, temp_path):
        if not root:
            return

        temp_path.append(root.val)

        if not root.left and not root.right and target == sum(temp_path):
            paths.append(temp_path[:])

        self.dfs(root.left, target, paths, temp_path)
        self.dfs(root.right, target, paths, temp_path)

        temp_path.pop()
