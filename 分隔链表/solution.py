class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        less_dummy = ListNode(0)
        greater_dummy = ListNode(0)
        less_tail = less_dummy
        greater_tail = greater_dummy
        cur = head

        while cur:
            next_node = cur.next
            cur.next = None

            if cur.val < x:
                less_tail.next = cur
                less_tail = less_tail.next
            else:
                greater_tail.next = cur
                greater_tail = greater_tail.next

            cur = next_node

        less_tail.next = greater_dummy.next

        return less_dummy.next
