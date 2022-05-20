"""
Given an integer array nums, 
return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
"""
class Solution:
    """
    1. sort the array
    2. for every element in the array, do a two sum of the other elements in the array
        - two sum is done by two pointers, left and right.
        - if sum is larger than target sum, move right pointer to the left of the current element, and vice versa.
    - if sum is equal to target sum, add the triplet to the result list.
    """
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        return_array = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum < 0:
                    left += 1
                elif sum > 0:
                    right -= 1
                else:
                    return_array.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1

        return return_array