# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if root == None:
            return
        queue = []
        queue.append(root)
        flag = False
        ans = []
        while queue:
            level_len = len(queue)
            level_nodes = []
            for i in range(level_len):
                current = queue.pop(0)
                level_nodes.append(current.val)
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
            ans.insert(0,level_nodes)
        return ans