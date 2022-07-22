"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.
"""
from  typing import List
class Solution:
    """
    the product of all the elements of nums except nums[i] is equal to the product of the product of elements to the right of nums[i] and the product of elements to the left of nums[i]
    - at any point, the product of all the elements to the left of the current element is stored in prefix[i]
    - at any point, the product of all the elements to the right of the current element is stored in postfix[i]
    - the product of all the elements to the left of the current element is multiplied by the product of all the elements to the right of the current element
    - this product is stored in res[i]
    
    1. we create an array of length n, where each element is equal to 1.
    2. we initialize prefix[0] to 1, and postfix[n-1] to 1. 
        this is because the product of all the elements to the left of the first element and all the elements 
        to the right of the last element is 1(there are no elements before/after them).
    3. we iterate through the array, and for each element:
        - we store the prefix in the array
        - we update prefix[i] by multiplying it with the current element
    4. we iterate through the array in reverse order, and for each element:
        - we multiply the current prefix with the postfix in the array(this will be the returned value)
        - we update postfix by multiplying it with the current element
    - we return the array
    Complexity:
    Time: O(n)
    Space: O(1) - ignoring space usage of the return array
    """
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums))
        
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res

sn  = Solution()
print(sn.productExceptSelf([1,2,3,4]))