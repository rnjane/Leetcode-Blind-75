"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.
"""
class Solution:
    """
    - we start by initializing the current sum to 0, and taking the first element of the array as the maximum subarray.
    - we iterate through the array, and for each element:
        - if the current sum is less than 0, we set the current sum to 0(this happens if we encounter a negative number that negates the current sum)
        - we add the current element to the current sum
        - if the current sum is greater than the maximum subarray, we update the maximum subarray to the current sum
    - we return the maximum subarray
    Time - O(n)
    Space - O(1)
    """
    def maxSubArray(self, nums: List[int]) -> int:
        maximum_sub_array = nums[0]
        current_sum = 0

        for n in nums:
            if current_sum < 0:
                current_sum = 0
            current_sum += n
            maximum_sub_array = max(maximum_sub_array, current_sum)

        return maximum_sub_array