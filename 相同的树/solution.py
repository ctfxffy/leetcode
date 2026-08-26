class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        stack = [(p, q)]

        while stack:
            node_p, node_q = stack.pop()

            if not node_p and not node_q:
                continue

            if not node_p or not node_q:
                return False

            if node_p.val != node_q.val:
                return False

            stack.append((node_p.left, node_q.left))
            stack.append((node_p.right, node_q.right))

        return True
