# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        if root == None:
            return False
        queue = []
        queue.append(root)
        flag = False
        target = -1
        while queue:
            level_len = len(queue)
            level_nodes = []
            d = {}
            for i in range(level_len):
                current = queue.pop(0)
                level_nodes.append(current.val)
                if current.left:
                    d[current.left.val] = current.val
                    queue.append(current.left)
                if current.right:
                    d[current.right.val] = current.val
                    queue.append(current.right)
            if x in d and y in d and d[x]!=d[y]:
                return True
        return False