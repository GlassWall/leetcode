# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        queue = []
        queue.append(root)
        height = 1
        while queue:
            level_len = len(queue)
            for i in range(level_len):
                current = queue.pop(0)
                if current.left == None and current.right == None:
                    return height
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
            height = height + 1
        return height
