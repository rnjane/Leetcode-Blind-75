"""
Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, 
and return the product.

A subarray is a contiguous subsequence of the array.
O(n)/O(1) : Time/Memory
"""
class Solution:
    """
    - for every element in the array, we compute max_product_so_far and min_product_so_far.
    - max_product_so_far is the maximum product of all the elements in the subarray that ends with the current element.
    - min_product_so_far is the minimum product of all the elements in the subarray that ends with the current element.
        - the reason we keep track of min and max is to take care of negative numbers. 
        - a negative number will give us min product. if we find another negative number, 
            the min will be positive, and as such, we want to be able to take it into consideration.
    - we init max_product_so_far and min_product_so_far to 1: which is a neutral number in product operations.
    - we init return_var to max of the array.
    - for each element in the array:
        - we store max_product_so_far to a temp var(because it'll be updated) - tmp
        - we compute max_product_so_far: max of current element, current element * max_product_so_far, current element * min_product_so_far
        - we compute min_product_so_far: min of current element, current element * tmp, current element * min_product_so_far
        - we update return_var to max of return_var, max_product_so_far
    - return return_var
    """
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curMin, curMax = 1, 1
        
        for n in nums:
            tmp = curMax * n
            curMax = max(n * curMax, n * curMin, n) 
            curMin = min(tmp, n * curMin, n)
            res = max(res, curMax)
        return res