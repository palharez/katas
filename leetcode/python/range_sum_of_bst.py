class Solution:
    def range_sum_bst(self, root, low: int, high: int) -> int:
        if root.val is None:
            return 0

        queue = []

        total = 0

        queue.append(root)

        while(len(queue) > 0):

            node = queue.pop(0)

            if node.val >= low and node.val <= high:
                total += node.val

            if node.left is not None:
                queue.append(node.left)

            if node.right is not None:
                queue.append(node.right)

        return total
