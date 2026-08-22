class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return None

        cur = head
        while cur:
            copy = Node(cur.val)
            copy.next = cur.next
            cur.next = copy
            cur = copy.next

        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next

        dummy = Node(0)
        copy_cur = dummy
        cur = head

        while cur:
            copy = cur.next
            next_node = copy.next

            copy_cur.next = copy
            copy_cur = copy

            cur.next = next_node
            cur = next_node

        return dummy.next
