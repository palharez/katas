class Solution:
    def sumOfLeftLeaves(self, root) -> int:
        summed = 0

        queue = [(root, False)]

        while queue:
            curr, is_left = queue.pop(0)

            if not curr.left and not curr.right and is_left:
                summed += curr.val

            if curr.left:
                queue.append((curr.left, True))

            if curr.right:
                queue.append((curr.right, False))

        return summed
