"""
Given head, the head of a linked list, determine if the linked list has a cycle in it.
There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. 
Internally, pos is used to denote the index of the node that tail's next pointer is connected to. 
Note that pos is not passed as a parameter.
"""
class Solution:
    """
    Create two pointers, and go through the l.list. one pointer is faster than the other.
    - if there is a loop, then at some point the two pointers will get to each other.
    - if the fast pointer gets to the end, there is no loop.
    """
    def hasCycle(self, head) -> bool:
        if head is None:
            return False
        pointer_1 = head
        pointer_2 = head.next
        while pointer_1 != pointer_2:
            if pointer_2 == None or pointer_2.next == None:
                return False
            else:
                pointer_1 = pointer_1.next
                pointer_2 = pointer_2.next.next
        return True
    
    """
    Complexity analysis

    Time complexity : O(n)O(n). Let us denote nn as the total number of nodes in the linked list. To analyze its time complexity, we consider the following two cases separately.

    List has no cycle:
    The fast pointer reaches the end first and the run time depends on the list's length, which is O(n).

    Space complexity : O(1). We only use two nodes (slow and fast) so the space complexity is O(1).
    """