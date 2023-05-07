def hasPathSum(self, root, targetSum: int) -> bool:
    if not root:
        return False
    if root.left == None and root.right == None and targetSum - root.val == 0:
        return True
    else:
        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)
