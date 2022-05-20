# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        we use two pointers, left initialized to a dummy node(with its next pointing to head) and right initialized to head + n steps
        - we use dummy node so that when we find the nth node, the left pointer is actually pointing to the previous of the nth node
        we move forward until right pointer reaches the end of the list
        - we then set next of the left pointer to left.next.next, thereby bypassing the nth node
        - return dummy.next
        """
        dummy_node = ListNode(0, head)
        left = dummy_node
        right = head
        for _ in range(n):
            right = right.next

        while right is not None:
            left = left.next
            right = right.next

        left.next = left.next.next
        return dummy_node.next

"""
Time complexity : O(n). Assume that n is the list's length, the time complexity is O(n).
Space complexity : O(1).
"""