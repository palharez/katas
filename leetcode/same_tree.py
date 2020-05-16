class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p, q):

        stack = []

        def dfs(root):

            if root == None:
                return

            stack.append(root.val)

            if not root.right and not root.left:
                return

            if root.left == None:
                stack.append(None)
            else:
                dfs(root.left)

            dfs(root.right)

        dfs(p)
        stack_p = stack[::]

        stack = []
        dfs(q)

        return stack == stack_p
