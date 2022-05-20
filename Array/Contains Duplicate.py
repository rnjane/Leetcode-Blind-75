"""
Utilize a dynamic data structure that supports fast search and insert operations(set).

- we use a set to store the elements of the array.
- we loop through the array and check if the element is in the set.
- if the element is not in the set, we add it to the set.
- if the element is in the set, we return True.
- if we have not returned True, we return False.
"""
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False
"""
Complexity Analysis

Time complexity: O(n). We do search() and insert() for n times and each operation takes constant time.

Space complexity: O(n). The space used by a set is linear with the number of elements in it.
"""