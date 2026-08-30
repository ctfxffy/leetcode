class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        inorder_index = {}
        for i, value in enumerate(inorder):
            inorder_index[value] = i

        self.postorder_index = len(postorder) - 1

        def build(left, right):
            if left > right:
                return None

            root_val = postorder[self.postorder_index]
            self.postorder_index -= 1
            root = TreeNode(root_val)

            mid = inorder_index[root_val]
            root.right = build(mid + 1, right)
            root.left = build(left, mid - 1)

            return root

        return build(0, len(inorder) - 1)
