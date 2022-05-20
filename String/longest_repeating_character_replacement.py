"""
We use sliding window approach to solve this problem.
longest_substring_without_repeating_characters = 0
1. Starting from the beginning of the list, we move the window forward by one node at a time.
- we create a hash map of the elements in the current window and their frequencies.
- if len(current_window) - frequency of the most popular element in the current window is less than or equal to k, we move the right pointer forward.
    - longest_substring_without_repeating_characters = max(longest_substring_without_repeating_characters, len(current_window))
- if len(current_window) - frequency of the most popular element in the current window is greater than k, we move the right pointer forward.
"""
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        current_window = {}
        longest_substring_without_repeating_characters = 0
        left_pointer = 0
        right_pointer = 0
        while right_pointer < len(s):
            current_window[s[right_pointer]] = current_window.get(s[right_pointer], 0) + 1
            if (right_pointer - left_pointer + 1) - max(current_window.values()) > k:
                current_window[s[left_pointer]] -= 1
                left_pointer += 1
            longest_substring_without_repeating_characters = max(longest_substring_without_repeating_characters, right_pointer - left_pointer + 1)
            right_pointer += 1
        return longest_substring_without_repeating_characters

"""
Complexity Analysis
Time - O(n)
Space - O(1)
"""