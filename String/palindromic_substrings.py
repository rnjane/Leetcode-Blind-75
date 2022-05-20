class Solution:
    """
    we initialize number_of_substrings to 0
    we loop through the indices of string s
    - palindromes can either be even or odd length
    - for even length palindromes, we pass the current index and the index + 1 to the helper function. we add the result to number_of_substrings.
    - for odd length palindromes, we pass the current index twice(as left and right) to the helper function. we add the result to number_of_substrings.
    we return number_of_substrings

    helper function:
    we initialize number_of_substrings to 0
    - we check if the indices are within the bounds of the string
    - we check if the characters at the indices are equal
    - if the characters are equal, we increment number_of_substrings by 1 and expand the sunstring outwards.
    - if the characters are not equal, we return number_of_substrings
    """
    def countSubstrings(self, s: str) -> int:
        number_of_substrings = 0
        for i in range(len(s)):
            number_of_substrings += self.count_palindromic_substrings_at_the_given_indices(s, i, i)
            number_of_substrings += self.count_palindromic_substrings_at_the_given_indices(s, i, i + 1)
        return number_of_substrings

    def count_palindromic_substrings_at_the_given_indices(self, s: str, left: int, right: int) -> int:
        number_of_substrings = 0
        while left >= 0 and right < len(s) and s[left] == s[right]:
            number_of_substrings += 1
            left -= 1
            right += 1
        return number_of_substrings