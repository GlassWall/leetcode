class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if len(preorder)==0:
            return None
        smaller = []
        greater = []
        root = TreeNode(preorder[0])
        for i in range(1,len(preorder)):
            if preorder[i]<root.val:
                smaller.append(preorder[i])
            else:
                greater.append(preorder[i])

        root.left = self.bstFromPreorder(preorder=smaller)
        root.right = self.bstFromPreorder(preorder=greater)
        return root