class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        """
        - we create two vars: prev and curr
        - initialize prev to None, and curr to head
        - while curr is not None:
            - create a temp variable(temp_next) to hold curr.next
            - set curr.next to prev
            - set prev to curr
            - set curr to temp_next
        - return prev
        """
        previous_node = None
        current_node = head
        while current_node is not None:
            temp_next = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = temp_next
        return previous_node

    """
    Complexity analysis
    Time complexity : O(n). Assume that n is the list's length, the time complexity is O(n).
    Space complexity : O(1).
    """


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        """
        recursive approach
        - for base case, we check if current is none(to take care of empty list) or if current.next is none(to take care of getting to the end of the list)
            - if either of these is true, we return head
        - otherwise, we call the function on head.next, and set new_head to the returned value of that call
        - head.next.next = head will set the next of the current node to the previous node
        - head.next = None is to avoid having two next pointers pointing each other * 
        - return current
        """
        if head is None or head.next is None:
            return head
        else:
            new_head = self.reverseList(head.next)
            head.next.next = head
            head.next = None
            return new_head

    """
    Complexity Analysis
    Time complexity : O(n). Assume that nn is the list's length, the time complexity is O(n).
    Space complexity : O(n). The extra space comes from implicit stack space due to recursion. The recursion could go up to n levels deep.
    """
