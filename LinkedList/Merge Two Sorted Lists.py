"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:

Input: list1 = [], list2 = []
Output: []

Example 3:

Input: list1 = [], list2 = [0]
Output: [0]

Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
    1. create an empty node
    2. if l1.val < l2.val:
        empty_nnode.next = l1
        l1 = l1.next
    else:
        empty_nnode.next = l2
        l2 = l2.next
    3. while l1 or l2:
        if l1.val < l2.val:
            empty_nnode.next = l1
            l1 = l1.next
        else:
            empty_nnode.next = l2
            l2 = l2.next
    4. return empty_nnode.next
    """
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        empty_node = ListNode()
        current_node = empty_node
        while l1 is not None or l2 is not None:
            if l1 is None:
                current_node.next = l2
                break
            elif l2 is None:
                current_node.next = l1
                break
            elif l1.val < l2.val:
                current_node.next = l1
                l1 = l1.next
            else:
                current_node.next = l2
                l2 = l2.next
            current_node = current_node.next
        return empty_node.next