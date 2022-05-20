"""
You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.
"""
"""
The solution here is:
1. divide the list into two equal(or almost equal)parts.
2. reverse the second part.
3. merge the two parts, in the order:
    - element in the first part points to the next element in the second part, then back to the first part, and so on.

- Dividing the list into two parts:
    - use two pointers, a slow pointer and a fast pointer.
    - slow pointer moves one step each time, while fast pointer moves two steps each time.
    - when fast pointer reaches the end of the list, slow pointer is in the middle of the list.
    - second list starts at slow.next and ends at fast.next.next.
- Reversing the second part:
    - store the next of the first element in a temp variable.
    - point the next of the first element in the second list to None.
    - point the temp variable to the next of the second list.
    - continue until the second list is reversed.
- Merging the two parts:
    - use two pointers, one for each list.
    - point the next of the first element in the first list to the next of the second list.
    - point the next of the first element in the second list to the next of the first list.
    - continue until the second list is empty.

Time complexity: O(n)
Space complexity: O(1)
"""
class Solution:
    def reorderList(self, head: ListNode) -> None:
        # find middle
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # reverse second half
        second = slow.next
        prev = slow.next = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        
        # merge two halfs
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2