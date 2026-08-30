class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        inorder_index = {}
        for i, value in enumerate(inorder):
            inorder_index[value] = i

        self.preorder_index = 0

        def build(left, right):
            if left > right:
                return None

            root_val = preorder[self.preorder_index]
            self.preorder_index += 1
            root = TreeNode(root_val)

            mid = inorder_index[root_val]
            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)

            return root

        return build(0, len(inorder) - 1)
