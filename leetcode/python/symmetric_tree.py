class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def __init__(self):
        self.ans = True

    def isSymmetric(self, root):

        def dfs(node_one, node_two):

            if not node_one and not node_two:
                return

            if not node_one and node_two or node_one and not node_two:
                self.ans = False
                return

            if node_one.val != node_two.val:
                self.ans = False
                return

            dfs(node_one.left, node_two.right)
            dfs(node_one.right, node_two.left)

        if not root:
            return self.ans

        dfs(root.left, root.right)

        return self.ans
