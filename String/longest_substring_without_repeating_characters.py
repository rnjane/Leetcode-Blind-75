"""
Given a string s, find the length of the longest substring without repeating characters.
"""
class Solution:
    """
    we use sliding window to solve this problem.
    we use a set to store the characters in the current window.
    if the set contains the current character, we remove the leftmost character in the set and add the new character to the set.
    if the current character is not in the set, we add it to the set, and compute the length of the set. 
    - if the length is larger than the maximum length, we update the maximum length.
    we retutn the maximum length.
    """
    def lengthOfLongestSubstring(self, s: str) -> int:
        sliding_window = set()
        max_length = 0
        left = 0
        for char in s:
            if char in sliding_window:
                while char in sliding_window:
                    sliding_window.remove(s[left])
                    left += 1
            else:
                pass
            sliding_window.add(char)
            max_length = max(max_length, len(sliding_window))
        return max_length

"""
Complexity Analysis

Time complexity : O(2n) = O(n)O(2n)=O(n). In the worst case each character will be visited twice by i and j.

Space complexity : O(min(m, n)). where m is the number of alphabets(26)
"""