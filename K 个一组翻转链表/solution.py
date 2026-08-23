class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        group_prev = dummy

        while True:
            kth = group_prev
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next

            group_next = kth.next
            prev = group_next
            cur = group_prev.next

            while cur != group_next:
                next_node = cur.next
                cur.next = prev
                prev = cur
                cur = next_node

            new_group_tail = group_prev.next
            group_prev.next = kth
            group_prev = new_group_tail
